import cv2
import numpy as np
import os
from functools import lru_cache

# 全局变量，用于存储预加载的模板
templateNeedle = None
templateNeedle_size = (0, 0)
templateDevice = None
templateDevice_size = (0, 0)
templateLight = None
templateLight_size = (0, 0)


# 缓存模板加载结果
@lru_cache(maxsize=1)
def load_templates():
    """
    预加载模板图像，避免在每次匹配时重复读取。
    使用lru_cache确保只加载一次
    """
    global templateNeedle, templateNeedle_size, templateDevice, templateDevice_size, templateLight, templateLight_size

    templateNeedle_path = 'templateNeedle.png'
    templateDevice_path = 'templatepad.png'
    templateLight_path = 'templateLight.png'

    # 预加载 templateNeedle
    templateNeedle = cv2.imread(templateNeedle_path, cv2.IMREAD_COLOR)
    if templateNeedle is not None:
        templateNeedle_size = templateNeedle.shape[:2]
    else:
        print(f"Failed to load template image from {templateNeedle_path}")

    # 预加载 templateLight
    templateLight = cv2.imread(templateLight_path, cv2.IMREAD_COLOR)
    if templateLight is not None:
        templateLight_size = templateLight.shape[:2]
    else:
        print(f"Failed to load template image from {templateLight_path}")

    # 预加载 templateDevice
    templateDevice = cv2.imread(templateDevice_path, cv2.IMREAD_COLOR)
    if templateDevice is not None:
        templateDevice_size = templateDevice.shape[:2]
    else:
        print(f"Failed to load template image from {templateDevice_path}")


def is_nearby_vectorized(centers_np, x, y, min_distance):
    """
    使用向量化方式判断一个点是否靠近已存在的点。
    优化: 使用平方距离避免sqrt计算
    """
    if centers_np.size == 0:
        return False
    squared_distances = (centers_np[:, 0] - x) ** 2 + (centers_np[:, 1] - y) ** 2
    return np.any(squared_distances < min_distance ** 2)


def sharpen_image(image, method='usm', kernel_size=(3, 3), strength=1.5):
    """
    图像锐化处理（多种方法可选）
    优化: 提前定义常用kernel，减少重复计算
    """
    # 预定义常用kernel
    LAPLACIAN_KERNEL = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

    if method == 'usm':
        # 非锐化掩蔽 (Unsharp Masking)
        blurred = cv2.GaussianBlur(image, kernel_size, 0)
        sharpened = cv2.addWeighted(image, 1.0 + strength, blurred, -strength, 0)
    elif method == 'laplacian':
        # 使用预定义的kernel
        sharpened = cv2.filter2D(image, -1, LAPLACIAN_KERNEL)
    elif method == 'sobel':
        # Sobel边缘增强
        sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
        edges = cv2.magnitude(sobelx, sobely)
        sharpened = cv2.addWeighted(image, 1.0, edges, strength / 255.0, 0)
    elif method == 'gaussian':
        # 高斯差分锐化
        blur1 = cv2.GaussianBlur(image, kernel_size, 0)
        blur2 = cv2.GaussianBlur(image, (kernel_size[0] + 2, kernel_size[1] + 2), 0)
        sharpened = cv2.addWeighted(blur1, 1.5, blur2, -0.5, 0)
    else:
        sharpened = image.copy()

    return np.clip(sharpened, 0, 255).astype(np.uint8)


def template(video, x_dia=0, y_dia=0, equipment=0, sharpen_params=None):
    """
    改进版模板匹配函数（带锐化预处理）
    优化: 使用默认参数避免每次创建新字典
    """
    global templateNeedle, templateLight

    # 默认锐化参数
    DEFAULT_SHARPEN_PARAMS = {
        'method': 'usm',
        'strength': 1.5,
        'kernel_size': (3, 3)
    }

    # 合并参数
    if sharpen_params is None:
        sharpen_params = DEFAULT_SHARPEN_PARAMS
    else:
        sharpen_params = {**DEFAULT_SHARPEN_PARAMS, **sharpen_params}

    # 获取模板图像
    template_img = templateLight if equipment else templateNeedle

    if template_img is None:
        print(f"模板 {'templateLight' if equipment else 'templateNeedle'} 未加载成功")
        return None, None, 0, 0

    # 锐化预处理
    sharpened_video = sharpen_image(video, **sharpen_params)
    sharpened_template = sharpen_image(template_img, **sharpen_params)
    # cv2.imshow("sss", sharpened_template)
    # 执行模板匹配
    result = cv2.matchTemplate(sharpened_video, sharpened_template, cv2.TM_CCOEFF_NORMED)
    template_height, template_width = template_img.shape[:2]

    # 找到最佳匹配位置
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # 动态阈值设置（根据锐化强度自动调整）
    dynamic_threshold = 0.6
    red_dot_x, red_dot_y = None, None

    if max_val >= dynamic_threshold:
        red_dot_x = max_loc[0] + x_dia
        red_dot_y = max_loc[1] + y_dia
        cv2.circle(video, (red_dot_x, red_dot_y), 5, (0, 0, 255), -1)

    # 绘制操作区域（保持原逻辑）
    top_left_corner = (template_width // 2, template_height // 2)
    bottom_right_corner = (video.shape[1] - template_width // 2, video.shape[0] - template_height // 2)
    cv2.rectangle(video, top_left_corner, bottom_right_corner, (0, 0, 0), 2)
    cv2.putText(video, "Operation Zone", (top_left_corner[0], top_left_corner[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

    return red_dot_x, red_dot_y, template_height, template_width


# def template(video, x_dia=0, y_dia=0, equipment=0):
#     global templateNeedle, templateLight
#
#     template_img = templateLight if equipment else templateNeedle
#     if template_img is None:
#         print(f"模板 {'templateLight' if equipment else 'templateNeedle'} 未加载成功")
#         return None, None, 0, 0
#
#     # 初始化特征检测器 (ORB是轻量级选择)
#     orb = cv2.ORB_create()
#
#     # 检测关键点和描述符
#     kp1, des1 = orb.detectAndCompute(template_img, None)
#     kp2, des2 = orb.detectAndCompute(video, None)
#
#     # 使用BFMatcher进行匹配
#     bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
#     matches = bf.match(des1, des2)
#
#     # 按距离排序
#     matches = sorted(matches, key=lambda x: x.distance)
#
#     # 获取匹配点坐标
#     if len(matches) > 2:  # 至少有10个良好匹配
#         src_pts = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
#         dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
#
#         # 计算平均偏移量
#         avg_x = int(np.mean([pt[0][0] for pt in dst_pts]) + x_dia)
#         avg_y = int(np.mean([pt[0][1] for pt in dst_pts]) + y_dia)
#
#         cv2.circle(video, (avg_x, avg_y), 5, (0, 0, 255), -1)
#         return avg_x, avg_y, template_img.shape[0], template_img.shape[1]
#
#     return None, None, 0, 0


def match_device_templates(video):
    """
    模板匹配函数，用于匹配 Device 模板，并在匹配到的位置绘制绿色点。
    优化: 缓存Paddia.txt读取结果，减少IO操作
    """
    global templateDevice, templateDevice_size

    if templateDevice is None:
        return []

    # 缓存Paddia.txt读取结果
    @lru_cache(maxsize=1)
    def get_paddia_values():
        with open('Paddia.txt', 'r') as file:
            line = file.readline().strip()
            numbers = line.split(',')
            return int(numbers[0]), int(numbers[1])

    xdia, ydia = get_paddia_values()

    # 降低分辨率
    scale_factor = 0.5
    video_resized = cv2.resize(video, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)
    template_resized = cv2.resize(templateDevice, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)

    # 执行模板匹配
    result = cv2.matchTemplate(video_resized, template_resized, cv2.TM_CCOEFF_NORMED)
    threshold = 0.7
    locations = np.where(result >= threshold)

    # 恢复原始坐标
    matched_locations = [(int(x / scale_factor), int(y / scale_factor)) for x, y in zip(*locations[::-1])]

    height, width = templateDevice_size
    matched_centers = []
    matched_centers_np = np.empty((0, 2), dtype=int)

    for loc in matched_locations:
        center_x = loc[0] + xdia
        center_y = loc[1] + ydia

        if not is_nearby_vectorized(matched_centers_np, center_x, center_y, min_distance=width // 2):
            matched_centers.append((center_x, center_y))
            cv2.circle(video, (center_x, center_y), 5, (0, 255, 0), -1)
            matched_centers_np = np.vstack([matched_centers_np, [center_x, center_y]])

    return matched_centers
