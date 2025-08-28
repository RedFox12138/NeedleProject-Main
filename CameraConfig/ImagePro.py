import cv2
import numpy as np
from functools import lru_cache

# 全局变量，用于存储预加载的模板
templateNeedle = None
templateNeedle_size = (0, 0)
templateDevice = None
templateDevice_size = (0, 0)
templateLight = None
templateLight_size = (0, 0)


# 缓存模板加载结果
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


# def sharpen_image(image, method='usm', kernel_size=(3, 3), strength=1.5):
#     """
#     图像锐化处理（多种方法可选）
#     优化: 提前定义常用kernel，减少重复计算
#     """
#     # 预定义常用kernel
#     LAPLACIAN_KERNEL = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
#
#     if method == 'usm':
#         # 非锐化掩蔽 (Unsharp Masking)
#         blurred = cv2.GaussianBlur(image, kernel_size, 0)
#         sharpened = cv2.addWeighted(image, 1.0 + strength, blurred, -strength, 0)
#     elif method == 'laplacian':
#         # 使用预定义的kernel
#         sharpened = cv2.filter2D(image, -1, LAPLACIAN_KERNEL)
#     elif method == 'sobel':
#         # Sobel边缘增强
#         sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
#         sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
#         edges = cv2.magnitude(sobelx, sobely)
#         sharpened = cv2.addWeighted(image, 1.0, edges, strength / 255.0, 0)
#     elif method == 'gaussian':
#         # 高斯差分锐化
#         blur1 = cv2.GaussianBlur(image, kernel_size, 0)
#         blur2 = cv2.GaussianBlur(image, (kernel_size[0] + 2, kernel_size[1] + 2), 0)
#         sharpened = cv2.addWeighted(blur1, 1.5, blur2, -0.5, 0)
#     else:
#         sharpened = image.copy()
#
#     return np.clip(sharpened, 0, 255).astype(np.uint8)


# def template(video, x_dia=0, y_dia=0, equipment=0, sharpen_params=None):
#     """
#     高性能模板匹配函数（强制灰度处理）
#     返回值保持: (red_dot_x, red_dot_y, template_height, template_width)
#     """
#     global templateNeedle, templateLight
#
#     # 1. 强制转换为灰度图像（性能关键！）
#     if len(video.shape) == 3:
#         video_gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
#     else:
#         video_gray = video
#
#     # 2. 获取模板并灰度化
#     template_img = templateLight if equipment else templateNeedle
#     if template_img is None:
#         return None, None, 0, 0
#
#     if len(template_img.shape) == 3:
#         template_gray = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)
#     else:
#         template_gray = template_img
#
#     # 3. 锐化预处理（可选）
#     if sharpen_params:
#         video_gray = sharpen_image(video_gray, **sharpen_params)
#         template_gray = sharpen_image(template_gray, **sharpen_params)
#
#     # 4. 单次匹配（平衡精度和性能）
#     res = cv2.matchTemplate(video_gray, template_gray, cv2.TM_CCOEFF_NORMED)
#     _, max_val, _, max_loc = cv2.minMaxLoc(res)
#
#     # 5. 结果处理（保持原返回值格式）
#     if max_val < 0.6:  # 置信度阈值
#         return None, None, template_img.shape[0], template_img.shape[1]
#
#     # 计算红点位置（保持原有逻辑）
#     h, w = template_gray.shape
#     red_dot_x = max_loc[0] + w // 2 + x_dia
#     red_dot_y = max_loc[1] + h // 2 + y_dia
#
#     cv2.circle(video, (red_dot_x, red_dot_y), 5, (0, 0, 255), -1)  # 绘制红点
#     return red_dot_x, red_dot_y, template_img.shape[0], template_img.shape[1]


import cv2
import numpy as np


def template(video, x_dia=0, y_dia=0, equipment=0, sharpen_params=None):
    """快速稳定的模板匹配版本（增强预处理）"""
    global templateNeedle, templateLight

    # 1. 强制转换为灰度图像
    if len(video.shape) == 3:
        video_gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
    else:
        video_gray = video

    # 2. 获取模板并灰度化
    template_img = templateLight if equipment else templateNeedle
    if template_img is None:
        return None, None, 0, 0

    if len(template_img.shape) == 3:
        template_gray = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)
    else:
        template_gray = template_img

    # 3. 图像预处理（关键改进！）
    video_gray, template_gray = preprocess_images(video_gray, template_gray, sharpen_params)

    # 4. 使用多方法验证
    methods = [cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR_NORMED]
    best_val = -1
    best_loc = None

    for method in methods:
        res = cv2.matchTemplate(video_gray, template_gray, method)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)

        if max_val > best_val:
            best_val = max_val
            best_loc = max_loc

    # 5. 局部精细化搜索
    if best_val > 0.9:
        x, y = best_loc
        h, w = template_gray.shape

        # 在匹配区域周围进行精细化搜索
        if x > 5 and y > 5 and x + w < video_gray.shape[1] - 5 and y + h < video_gray.shape[0] - 5:
            roi = video_gray[y - 5:y + h + 5, x - 5:x + w + 5]
            refined_res = cv2.matchTemplate(roi, template_gray, cv2.TM_CCOEFF_NORMED)
            _, refined_val, _, refined_loc = cv2.minMaxLoc(refined_res)

            if refined_val > best_val:
                x = x - 5 + refined_loc[0]
                y = y - 5 + refined_loc[1]
                best_val = refined_val

        red_dot_x = x + w // 2 + x_dia
        red_dot_y = y + h // 2 + y_dia
        cv2.circle(video, (red_dot_x, red_dot_y), 5, (0, 0, 255), -1)  # 绘制红点
        return red_dot_x, red_dot_y, template_img.shape[0], template_img.shape[1]

    return None, None, 0, 0


def preprocess_images(video_gray, template_gray, sharpen_params=None):
    """综合图像预处理函数"""
    # 默认锐化参数
    if sharpen_params is None:
        sharpen_params = {'kernel_size': 3, 'sigma': 1.0, 'amount': 1.5, 'threshold': 10}

    # 1. 直方图均衡化（增强对比度）
    video_gray = cv2.equalizeHist(video_gray)
    template_gray = cv2.equalizeHist(template_gray)

    # 2. 高斯模糊去噪（轻微）
    video_gray = cv2.GaussianBlur(video_gray, (3, 3), 0)
    template_gray = cv2.GaussianBlur(template_gray, (3, 3), 0)

    # 3. 锐化处理
    video_gray = sharpen_image(video_gray, **sharpen_params)
    template_gray = sharpen_image(template_gray, **sharpen_params)

    # 4. 边缘增强（可选，对于边缘明显的探针很有效）
    video_gray = enhance_edges(video_gray)
    template_gray = enhance_edges(template_gray)

    return video_gray, template_gray


def sharpen_image(image, kernel_size=3, sigma=1.0, amount=1.5, threshold=5):
    """USM锐化算法"""
    # 高斯模糊
    blurred = cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)

    # 非锐化掩蔽
    sharpened = cv2.addWeighted(image, 1.0 + amount, blurred, -amount, 0)

    # 阈值处理，避免过度锐化平滑区域
    if threshold > 0:
        low_contrast_mask = np.abs(image - blurred) < threshold
        sharpened[low_contrast_mask] = image[low_contrast_mask]

    return sharpened


def enhance_edges(image, low_threshold=50, high_threshold=150):
    """边缘增强"""
    # Canny边缘检测
    edges = cv2.Canny(image, low_threshold, high_threshold)

    # 将边缘叠加到原图
    enhanced = cv2.addWeighted(image, 0.8, edges, 0.2, 0)

    return enhanced


# 可选：自适应预处理（根据图像特性自动调整）
def adaptive_preprocess(image):
    """自适应预处理"""
    # 计算图像对比度
    mean, std = cv2.meanStdDev(image)
    contrast = std[0][0]

    if contrast < 25:  # 低对比度图像
        image = cv2.equalizeHist(image)
        image = sharpen_image(image, amount=2.0)
    elif contrast > 60:  # 高对比度图像
        image = cv2.GaussianBlur(image, (3, 3), 0)
    else:  # 中等对比度
        image = sharpen_image(image, amount=1.5)

    return image


def match_device_templates(video):
    global templateDevice, templateDevice_size

    if templateDevice is None:
        print("模板未加载，无法进行匹配")
        return []

    try:
        with open('Paddia.txt', 'r') as f:
            xdia, ydia = map(int, f.read().strip().split(','))
    except:
        xdia, ydia = 0, 0



    # 灰度转换
    video_gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY) if len(video.shape) == 3 else video
    template_gray = cv2.cvtColor(templateDevice, cv2.COLOR_BGR2GRAY) if len(
        templateDevice.shape) == 3 else templateDevice

    # 记录原始模板尺寸（用于后续偏移量计算）
    original_template_h, original_template_w = template_gray.shape

    # 多尺度匹配
    scales = [0.8, 0.9, 1.0, 1.1, 1.2]
    all_matches = []

    for scale in scales:
        # 缩放模板
        if scale != 1.0:
            new_w = int(original_template_w * scale)
            new_h = int(original_template_h * scale)
            if new_w < 10 or new_h < 10: continue
            template_resized = cv2.resize(template_gray, (new_w, new_h))
        else:
            template_resized = template_gray

        # 执行匹配
        res = cv2.matchTemplate(video_gray, template_resized, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # 动态阈值
        threshold = max(0.8, max_val * 0.8)
        locs = np.where(res >= threshold)

        for pt in zip(*locs[::-1]):
            all_matches.append({
                'pt': pt,
                'size': (template_resized.shape[1], template_resized.shape[0]),
                'score': res[pt[1], pt[0]],
                'scale': scale
            })

    # 非极大值抑制
    all_matches.sort(key=lambda x: x['score'], reverse=True)
    final_locations = []

    for match in all_matches:
        pt = match['pt']
        w, h = match['size']

        # 计算当前匹配的中心点（未加偏移）
        center_x = pt[0] + w // 2
        center_y = pt[1] + h // 2

        # 检查是否与已选区域重叠
        overlap = False
        for selected in final_locations:
            s_center_x, s_center_y, s_w, s_h = selected
            if (abs(center_x - s_center_x) < (w + s_w) // 2 and
                    abs(center_y - s_center_y) < (h + s_h) // 2):
                overlap = True
                break

        if not overlap:
            # 计算缩放后的实际偏移量（按比例缩放）

            # 最终目标点 = 匹配中心 + 缩放后的偏移量
            target_x = center_x + xdia
            target_y = center_y + ydia

            final_locations.append((target_x, target_y, w, h))

            # 可视化
            # cv2.rectangle(video, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
            cv2.circle(video, (target_x, target_y), 4, (0, 255, 255), -1)

    return [(x, y) for x, y, _, _ in final_locations]