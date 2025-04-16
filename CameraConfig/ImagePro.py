import cv2
import numpy as np
import os



# 全局变量，用于存储预加载的模板
templateNeedle = None
templateNeedle_size = (0, 0)
templateDevice = None
templateDevice_size = (0, 0)


def load_templates():
    """
    预加载模板图像，避免在每次匹配时重复读取。
    """
    global templateNeedle, templateNeedle_size, dia_needle,templateDevice, templateDevice_size,templateLight, templateLight_size,dia_light
    templateNeedle_path = 'templateNeedle.png'
    templateDevice_path = 'templatepad.png'
    templatLight_path = 'templateLight.png'

    # 预加载 templateNeedle
    templateNeedle = cv2.imread(templateNeedle_path, cv2.IMREAD_COLOR)
    if templateNeedle is None:
        print(f"Failed to load template image from {templateNeedle_path}")
    else:
        templateNeedle_size = templateNeedle.shape[:2]

    templateLight = cv2.imread(templatLight_path, cv2.IMREAD_COLOR)
    if templateLight is None:
        print(f"Failed to load template image from {templatLight_path}")
    else:
        templateLight_size = templateLight.shape[:2]

    # 预加载 templateDevice
    templateDevice = cv2.imread(templateDevice_path, cv2.IMREAD_COLOR)
    if templateDevice is None:
        print(f"Failed to load template image from {templateDevice_path}")
    else:
        templateDevice_size = templateDevice.shape[:2]


def is_nearby_vectorized(centers_np, x, y, min_distance):
    """
    使用向量化方式判断一个点是否靠近已存在的点。

    :param centers_np: NumPy数组，已存在的点坐标。
    :param x: 新点的x坐标。
    :param y: 新点的y坐标。
    :param min_distance: 最小距离阈值。
    :return: 布尔值，是否靠近。
    """
    if centers_np.size == 0:
        return False
    distances = np.sqrt((centers_np[:, 0] - x) ** 2 + (centers_np[:, 1] - y) ** 2)
    return np.any(distances < min_distance)




def sharpen_image(image, method='usm', kernel_size=(3, 3), strength=1.5):
    """
    图像锐化处理（多种方法可选）

    参数:
        image: 输入图像
        method: 锐化方法 ('usm'|'laplacian'|'sobel'|'gaussian')
        kernel_size: 卷积核尺寸
        strength: 锐化强度

    返回:
        锐化后的图像
    """
    if method == 'usm':
        # 非锐化掩蔽 (Unsharp Masking)
        blurred = cv2.GaussianBlur(image, kernel_size, 0)
        sharpened = cv2.addWeighted(image, 1.0 + strength, blurred, -strength, 0)
    elif method == 'laplacian':
        # 拉普拉斯锐化
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        sharpened = cv2.filter2D(image, -1, kernel)
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

    # 确保像素值在合法范围内
    return np.clip(sharpened, 0, 255).astype(np.uint8)


def template(video, x_dia=0, y_dia=0, equipment=0, sharpen_params={}):
    """
    改进版模板匹配函数（带锐化预处理）

    新增参数:
        sharpen_params: 锐化参数配置字典，例如:
            {
                'method': 'usm',  # 锐化方法
                'strength': 1.5,  # 锐化强度
                'kernel_size': (3,3)  # 卷积核大小
            }
    """
    global templateNeedle, templateLight
    red_dot_x, red_dot_y = None, None
    template_width, template_height = 0, 0

    # 默认锐化参数
    default_sharpen = {
        'method': 'usm',
        'strength': 1.5,
        'kernel_size': (3, 3)
    }
    sharpen_params = { ** default_sharpen,  ** sharpen_params}

    # 获取模板图像
    template_img = templateLight if equipment else templateNeedle
    if template_img is None:
        print(f"模板 {'templateLight' if equipment else 'templateNeedle'} 未加载成功")
        return red_dot_x, red_dot_y, template_width, template_height

    # 锐化预处理
    sharpened_video = sharpen_image(video,  ** sharpen_params)
    sharpened_template = sharpen_image(template_img,  ** sharpen_params)

    # 执行模板匹配
    result = cv2.matchTemplate(sharpened_video, sharpened_template, cv2.TM_CCOEFF_NORMED)
    template_height, template_width = template_img.shape[:2]

    # 找到最佳匹配位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 动态阈值设置（根据锐化强度自动调整）
    dynamic_threshold = 0.6

    if max_val >= dynamic_threshold:
        top_left = max_loc
        red_dot_x = top_left[0] + x_dia
        red_dot_y = top_left[1] + y_dia

        # 绘制结果
        cv2.circle(video, (red_dot_x, red_dot_y), 5, (0, 0, 255), -1)

    # 绘制操作区域（保持原逻辑）
    top_left_corner = (template_width // 2, template_height // 2)
    bottom_right_corner = (video.shape[1] - template_width // 2, video.shape[0] - template_height // 2)
    cv2.rectangle(video, top_left_corner, bottom_right_corner, (0, 0, 0), 2)
    cv2.putText(video, "Operation Zone", (top_left_corner[0], top_left_corner[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

    return red_dot_x, red_dot_y, template_height, template_width


def match_device_templates(video):
    """
    模板匹配函数，用于匹配 Device 模板，并在匹配到的位置绘制绿色点。
    :param video: 输入的视频帧。
    :return: 返回匹配到的中心点和推挤点的列表。
    """
    global templateDevice, templateDevice_size
    matched_centers = []

    if templateDevice is None:
        return matched_centers

    # 降低分辨率
    scale_factor = 0.5  # 根据需要调整
    video_resized = cv2.resize(video, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)
    template_resized = cv2.resize(templateDevice, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)

    # 执行模板匹配
    result = cv2.matchTemplate(video_resized, template_resized, cv2.TM_CCOEFF_NORMED)
    threshold = 0.7
    locations = np.where(result >= threshold)

    # 恢复原始坐标
    matched_locations = [(int(x / scale_factor), int(y / scale_factor)) for x, y in zip(*locations[::-1])]

    height, width = templateDevice_size
    matched_centers_np = np.empty((0, 2), dtype=int)

    with open('Paddia.txt', 'r') as file:
        line = file.readline().strip()  # 读取第一行并去除首尾空白字符
        # 将字符串按空格分割成列表
    numbers = line.split(',')
    # 将字符串转换为整数
    xdia = int(numbers[0])
    ydia = int(numbers[1])

    for loc in matched_locations:
        top_left = loc
        center_x = top_left[0] + xdia
        center_y = top_left[1] + ydia

        if not is_nearby_vectorized(matched_centers_np, center_x, center_y, min_distance=width // 2):
            matched_centers.append((center_x, center_y))
            cv2.circle(video, (center_x, center_y), 5, (0, 255, 0), -1)
            matched_centers_np = np.vstack([matched_centers_np, [center_x, center_y]])

    return matched_centers


def is_nearby(centers, x, y, min_distance):
    """
    判断一个点是否靠近已存在的点。

    :param centers: 已存在的点列表。
    :param x: 新点的x坐标。
    :param y: 新点的y坐标。
    :param min_distance: 最小距离阈值。
    :return: 布尔值，是否靠近。
    """
    for cx, cy in centers:
        distance = np.sqrt((cx - x) ** 2 + (cy - y) ** 2)
        if distance < min_distance:
            return True
    return False


def is_nearby_vectorized(centers_np, x, y, min_distance):
    """
    使用向量化方式判断一个点是否靠近已存在的点。

    :param centers_np: NumPy数组，已存在的点坐标。
    :param x: 新点的x坐标。
    :param y: 新点的y坐标。
    :param min_distance: 最小距离阈值。
    :return: 布尔值，是否靠近。
    """
    if centers_np.size == 0:
        return False
    distances = np.sqrt((centers_np[:, 0] - x) ** 2 + (centers_np[:, 1] - y) ** 2)
    return np.any(distances < min_distance)


