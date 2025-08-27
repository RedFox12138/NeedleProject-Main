import os
import subprocess
import sys

from QTneedle.QTneedle.DailyLogger import DailyLogger
from StopClass import StopClass

# 定义你要添加的库文件路径
custom_lib_path = "c:\\users\\administrator\\appdata\\local\\programs\\python\\python37\\lib\\site-packages"

# 将路径添加到 sys.path
if custom_lib_path not in sys.path:
    sys.path.append(custom_lib_path)
import cv2
import threading
import time

from datetime import datetime
import numpy as np
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from CameraConfig.CamOperation_class import CameraOperation
from CameraConfig.CameraParams_header import MV_CC_DEVICE_INFO_LIST
from CameraConfig.ImagePro import load_templates, template, match_device_templates
from CameraConfig.MvCameraControl_class import MV_GIGE_DEVICE, MV_USB_DEVICE, MvCamera
from LTDS import ReturnNeedleMove, WhileMove
from Microscope import ReturnZauxdll
from SerialPage import SIM928ConnectionThread, RelayConnectionThread, NeedelConnectionThread
from demo import Ui_MainWindow


def handle_coordinates(x, y):
    print(f"Received coordinates: x={x}, y={y}")

# 获取日志器实例
logger = DailyLogger()

global red_dot_x
global red_dot_y


class MainPage1(QMainWindow, Ui_MainWindow):
    micro_distanceY = 0.5
    micro_distanceX = 0.5
    needle_distanceY = 300
    needle_distanceX = 300
    needle_distanceZ = 300

    obj_cam_operation = None
    equipment = 0  # 0代表电探针，1代表光纤
    stop_flag = False
    stop_num = 0
    # 默认的脚本位置
    import_script = "./jiaoben.py"
    # 默认的保存路径
    save_script = 'D:\\lzg\\data\\' + time.strftime("save_%Y-%m-%d_%H-%M-%S") + '\\IV\\'

    #全局的视频帧，为了让其他类也能调用截图
    global_frame = None

    # 给小灯设置颜色
    def get_stylesheet(status):
        color = "red" if status else "green"
        return f"""
               QLabel {{
                   background-color: {color};
                   border-radius: 20px;
                   border: 1px solid black;
               }}
           """

    def __init__(self, label_video, label_cameraLabel, Button_screenshot, lineEdit_savePath, Button_browse,
                 Button_needleTemplate,
                 Button_padTemplate, Button_iuCalculate, plainTextEdit_log, log_file,Checkbox_templateDevice,
                 Checkbox_microAutoTrace,Checkbox_ElecNeedle, Checkbox_Light,
                 Button_Micro_up, Button_Micro_down, Button_Micro_left, Button_Micro_right,
                 Button_needle1Up, Button_needle1Down, Button_needle1Left, Button_needle1Right,
                 lineEdit_needle1Xdistance, lineEdit_needle1Ydistance, lineEdit_needle1Zdistance,
                 Button_needle1SetXdisConfirm, Button_needle1SetYdisConfirm, Button_needle1SetZdisConfirm,
                 label_light,
                 lineEdit_SIM928, Button_SIM928,
                 Button_pushing, Button_pulling,
                 Button_relay, label_needle1, lineEdit_SaveResult,
                 lineEdit_needleSetXdis, lineEdit_needleSetYdis,lineEdit_needleSetZdis,
                 lineEdit_microSetXdis, lineEdit_microSetYdis,lineEdit_Scripts
                 ):
        super().__init__()
        self.lineEdit_Scripts = lineEdit_Scripts

        self.lineEdit_needleSetXdis = lineEdit_needleSetXdis
        self.lineEdit_needleSetYdis = lineEdit_needleSetYdis
        self.lineEdit_needleSetZdis = lineEdit_needleSetZdis
        self.lineEdit_microSetXdis = lineEdit_microSetXdis
        self.lineEdit_microSetYdis = lineEdit_microSetYdis

        MainPage1.micro_distanceX = float(self.lineEdit_microSetXdis.text())
        MainPage1.micro_distanceY = float(self.lineEdit_microSetYdis.text())
        MainPage1.needle_distanceY = float(self.lineEdit_needleSetYdis.text())
        MainPage1.needle_distanceX = float(self.lineEdit_needleSetXdis.text())
        MainPage1.needle_distanceZ = float(self.lineEdit_needleSetZdis.text())

        # 是否显示器件的模板匹配，True显示，False不显示
        self.DeviceTemplate_view = False

        # 调用电学测量函数，传入保存路径
        self.lineEdit_SaveResult = lineEdit_SaveResult

        # 电和光的选择按钮
        self.label_needle1 = label_needle1

        self.Checkbox_ElecNeedle = Checkbox_ElecNeedle
        self.Checkbox_Light = Checkbox_Light

        self.voltage928max = 0

        # 日志的路径
        self.log_file = log_file

        # 保存图片的默认路径
        self.save_folder = "./"

        # 刚开始默认显微镜不跟随
        self.align_allowed = False
        self.allow_alignment = True  # 控制对齐是否允许的标志

        # 初始化指示灯
        self.indicator = label_light
        self.status = False
        self.indicator.setStyleSheet(MainPage1.get_stylesheet(self.status))

        # 显微镜移动方向
        self.microY = 0
        self.microX = 1
        self.microup = -1
        self.microdown = 1
        self.microleft = 1
        self.microright = -1

        # 探针移动方向
        self.needleup = 0
        self.needledown = 1
        self.needleuleft = 2
        self.needleright = 3

        self.deviceList = MV_CC_DEVICE_INFO_LIST()
        self.cam = MvCamera()

        self.x_dia = 0
        self.y_dia = 0
        self.dia = np.zeros([2, 2])

        self.pad_x_dia = 0
        self.pad_y_dia = 0
        self.initCamera()
        self.timer = QTimer()
        self.label_video = label_video

        self.label_video.mousePressEvent = self.mousePressEvent

        self.label_cameraLabel = label_cameraLabel
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)
        self.frame_resized = 0
        self.lineEdit_savePath = lineEdit_savePath
        self.lineEdit_savePath.setText("C:\\Users\\Administrator\\PycharmProjects\\QTneedle\\ScreenShot")
        self.save_folder = "C:\\Users\\Administrator\\PycharmProjects\\QTneedle\\ScreenShot"

        self.plainTextEdit_log = plainTextEdit_log

        # 探针距离设置的输入框
        self.lineEdit_needle1Xdistance = lineEdit_needle1Xdistance
        self.lineEdit_needle1Ydistance = lineEdit_needle1Ydistance
        self.lineEdit_needle1Zdistance = lineEdit_needle1Zdistance

        self.lineEdit_needle1Xdistance.setText(str(MainPage1.needle_distanceX))
        self.lineEdit_needle1Ydistance.setText(str(MainPage1.needle_distanceY))
        self.lineEdit_needle1Zdistance.setText(str(MainPage1.needle_distanceZ))

        # 928更新电压
        self.lineEdit_SIM928 = lineEdit_SIM928
        Button_SIM928.clicked.connect(self.update_voltage)

        # 三个方向距离的确认按钮
        Button_needle1SetXdisConfirm.clicked.connect(self.update_needle_distanceX)
        Button_needle1SetYdisConfirm.clicked.connect(self.update_needle_distanceY)
        Button_needle1SetZdisConfirm.clicked.connect(self.update_needle_distanceZ)

        Button_screenshot.clicked.connect(lambda: threading.Thread(target=self.save_image).start())
        Button_browse.clicked.connect(self.browse_folder)
        Button_needleTemplate.clicked.connect(lambda: threading.Thread(target=self.select_template).start())
        Button_padTemplate.clicked.connect(lambda: threading.Thread(target=self.select_pad_template).start())
        Button_iuCalculate.clicked.connect(lambda: threading.Thread(target=self.CalIU()).start())

        # 显微镜是否跟随
        Checkbox_microAutoTrace.stateChanged.connect(self.checkbox_state_changed)

        # 是否显示探针的模板匹配
        Checkbox_templateDevice.stateChanged.connect(self.checkbox_template_changed)

        # 电探针和光的复选框
        self.Checkbox_ElecNeedle.toggled.connect(lambda: self.checkbox_ElecNeedle_changed(self.Checkbox_ElecNeedle))
        self.Checkbox_Light.toggled.connect(lambda: self.checkbox_Light_changed(self.Checkbox_Light))

        # 显微镜移动按钮
        Button_Micro_up.clicked.connect(self.move_microscope_up)
        Button_Micro_down.clicked.connect(self.move_microscope_down)
        Button_Micro_left.clicked.connect(self.move_microscope_left)
        Button_Micro_right.clicked.connect(self.move_microscope_right)

        # 探针移动按钮
        Button_needle1Up.clicked.connect(self.move_probe_up)
        Button_needle1Down.clicked.connect(self.move_probe_down)
        Button_needle1Left.clicked.connect(self.move_probe_left)
        Button_needle1Right.clicked.connect(self.move_probe_right)

        # 继电器的按钮
        Button_relay.clicked.connect(self.relay_IO)
        self.relay_flag = False

        Button_pushing.clicked.connect(lambda: threading.Thread(target=self.Pushing).start())
        Button_pulling.clicked.connect(lambda: threading.Thread(target=self.Pulling).start())

        self.log_timer = QTimer(self)
        self.log_timer.timeout.connect(self.update_log_display)
        self.log_timer.start(500)  # 每秒更新一次



    # 继电器的开关函数
    def relay_IO(self):
        try:
            if self.relay_flag:
                d = bytes.fromhex('A0 01 00 A1')  # 关闭
                RelayConnectionThread.anc.write(d)
                self.relay_flag = False
                time.sleep(0.1)
            else:
                d = bytes.fromhex('A0 01 01 A2')  # 打开
                RelayConnectionThread.anc.write(d)
                self.relay_flag = True
                time.sleep(0.1)
        except (AttributeError, ValueError):
            print("请检查继电器否连接")

    # @staticmethod
    def initCamera(self):
        # Enumerate devices
        ret = self.cam.MV_CC_EnumDevices(MV_GIGE_DEVICE | MV_USB_DEVICE, self.deviceList)
        if ret != 0:
            return

        if self.deviceList.nDeviceNum == 0:
            print("Find no device")
            return

        # Select the first device
        nSelCamIndex = 0
        # Open selected device
        MainPage1.obj_cam_operation = CameraOperation(self.cam, self.deviceList, nSelCamIndex)
        ret = MainPage1.obj_cam_operation.Open_device()
        if ret != 0:
            return
        # Start grabbing
        ret = MainPage1.obj_cam_operation.Start_grabbing(0)
        if ret != 0:
            return


    def update_frame(self):
        load_templates()

        stFrameInfo = MainPage1.obj_cam_operation.st_frame_info
        if MainPage1.obj_cam_operation.buf_grab_image_size > 0 and stFrameInfo:
            if stFrameInfo.nWidth > 0 and stFrameInfo.nHeight > 0 and stFrameInfo.nFrameLen > 0:
                try:
                    global red_dot_x, red_dot_y

                    data = np.frombuffer(MainPage1.obj_cam_operation.buf_grab_image, dtype=np.uint8,
                                         count=stFrameInfo.nFrameLen)

                    frame = data.reshape((stFrameInfo.nHeight, stFrameInfo.nWidth))
                    self.frame_resized = cv2.cvtColor(frame, cv2.COLOR_BayerBG2RGB)
                    self.frame_resized = cv2.resize(self.frame_resized,
                                                    (stFrameInfo.nWidth // 4, stFrameInfo.nHeight // 4),
                                                    interpolation=cv2.INTER_LINEAR)
                    self.frame_resized = cv2.resize(self.frame_resized, (851, 851), interpolation=cv2.INTER_LINEAR)

                    with open('dia' + str(MainPage1.equipment) + '.txt', 'r') as file:
                        line = file.readline().strip()  # 读取第一行并去除首尾空白字符
                    # 将字符串按空格分割成列表
                    numbers = line.split(',')
                    # 将字符串转换为整数
                    xdia = int(numbers[0])
                    ydia = int(numbers[1])

                    red_dot_x, red_dot_y, self.board_height, self.board_width = template(self.frame_resized, xdia,
                                                                                         ydia, MainPage1.equipment)


                    if self.DeviceTemplate_view:
                        match_device_templates(self.frame_resized)
                    self.frame_resized = self.align_frame_with_probe()

                    height, width, channel = self.frame_resized.shape
                    bytes_per_line = 3 * width
                    q_image = QImage(self.frame_resized.data, width, height, bytes_per_line, QImage.Format_BGR888)

                    self.label_video.setPixmap(QPixmap.fromImage(q_image))
                    # 提取中心区域
                    center_width, center_height = width // 2, height // 2

                    start_x, start_y = max(0, center_width // 2), max(0, center_height // 2)
                    q_image_zoom = q_image.copy(start_x, start_y, center_width, center_height)
                    self.label_cameraLabel.setPixmap(QPixmap.fromImage(q_image_zoom))

                    MainPage1.global_frame = self.frame_resized
                    return self.frame_resized

                except Exception as e:
                    print(f"Error updating frame: {e}")

    def browse_folder(self):
        # 打开文件夹选择对话框
        folder = QFileDialog.getExistingDirectory(self, "选择存储路径", "", QFileDialog.ShowDirsOnly)
        if folder:
            # 将选择的文件夹路径显示在文本框中
            self.lineEdit_savePath.setText(folder)
            self.save_folder = folder

    def save_image(self):
        frame = self.update_frame()
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        filename = f"{timestamp}.png"
        path = os.path.join(self.save_folder, filename)
        cv2.imwrite(path, frame)

    def match_and_move(self):
        # 获取当前帧并进行模板匹配
        video = self.update_frame()  # 这是一个假设函数，你需要从摄像头获取当前帧
        matched_centers = match_device_templates(video)

        if matched_centers:
            min_distance = float('inf')
            matched_centers = match_device_templates(video)
            probe_x, probe_y = self.get_probe_position()
            for center_x, center_y in matched_centers:
                distance = pow(abs(center_x - probe_x), 2) + pow(abs(center_y - probe_y), 2)
                if distance < min_distance:
                    min_distance = distance
                    closet = [center_x, center_y]
            self.move_probe_to_target(closet[0], closet[1])

    # 选择模板的函数
    def select_template(self):
        param = self.frame_resized
        r = cv2.selectROI("Select Needle Template", param, showCrosshair=True, fromCenter=False)

        # 检查用户是否取消选择或选择了无效的区域
        if r[2] == 0 or r[3] == 0:
            print("选择被取消或无效。")
            cv2.destroyWindow("Select Needle Template")
            return None

        global mouseX, mouseY
        mouseX = 0
        mouseY = 0

        # 定义鼠标回调函数
        def mouse_callback(event, X, Y, flags, userdata):
            if event == cv2.EVENT_LBUTTONDOWN:
                print(f"鼠标点击坐标: ({X}, {Y})")
                global mouseX, mouseY
                mouseX = X
                mouseY = Y

                # 解除回调
                cv2.setMouseCallback("Select Needle Template", lambda *args: None)  # 解除回调

        # 设置鼠标回调
        cv2.setMouseCallback("Select Needle Template", mouse_callback)

        # 使用一个小的等待时间，避免等待太长时间
        while True:
            # 以 1ms 的延迟等待键盘事件或鼠标点击
            key = cv2.waitKey(1)  # 不阻塞，避免长时间卡住
            if mouseX != 0 and mouseY != 0:  # 判断是否有鼠标点击
                break
            if key == 27:  # 监听 ESC 键退出
                print("用户按下 ESC 键退出。")
                cv2.destroyWindow("Select Needle Template")
                return None

        # 获取选中的矩形区域，并进行裁剪
        if r is not None:
            x, y, w, h = r
            cropped_image = param[y:y + h, x:x + w]
            if MainPage1.equipment:
                cv2.imwrite("templateLight.png", cropped_image)
            else:
                cv2.imwrite("templateNeedle.png", cropped_image)
            load_templates()
            red_dot_x, red_dot_y, _, _ = template(self.frame_resized, equipment=MainPage1.equipment)
            self.x_dia = mouseX - red_dot_x
            self.y_dia = mouseY - red_dot_y
            cv2.destroyWindow("Select Needle Template")

            with open('dia' + str(MainPage1.equipment) + '.txt', 'w') as f:
                f.write(f"{self.x_dia},{self.y_dia}")

    def take_screenshot(self):
        # 截取当前帧并让用户框选区域
        r = cv2.selectROI("Take Screenshot", self.frame_resized, showCrosshair=True, fromCenter=False)

        # 检查用户是否取消选择或选择了无效的区域
        if r[2] == 0 or r[3] == 0:
            print("框选被取消或无效。")
            cv2.destroyWindow("Take Screenshot")
            return None

        # 获取选中的矩形区域，并进行裁剪
        x, y, w, h = r
        cropped_image = self.frame_resized[y:y + h, x:x + w]

        # 保存截图
        cv2.imwrite("screenshot.png", cropped_image)
        print("截图已保存为 screenshot.png")
        cv2.destroyWindow("Take Screenshot")



    def select_pad_template(self):
        # 先截图并让用户框选区域
        self.take_screenshot()

        # 读取截图
        screenshot = cv2.imread("screenshot.png")
        if screenshot is None:
            print("无法读取截图，请检查文件路径。")
            return None

        # 让用户在截图上再次框选区域
        r = cv2.selectROI("Select Pad Template", screenshot, showCrosshair=True, fromCenter=False)

        # 检查用户是否取消选择或选择了无效的区域
        if r[2] == 0 or r[3] == 0:
            print("框选被取消或无效。")
            cv2.destroyWindow("Select Pad Template")
            return None

        # 获取选中的矩形区域，并进行裁剪
        x, y, w, h = r
        template_pad = screenshot[y:y + h, x:x + w]

        # 保存框选的区域为 templatePad.png
        cv2.imwrite("templatepad.png", template_pad)
        print("框选区域已保存为 templatePad.png")

        global mouseX, mouseY
        mouseX = 0
        mouseY = 0

        # 定义鼠标回调函数
        def mouse_callback(event, X, Y, flags, userdata):
            if event == cv2.EVENT_LBUTTONDOWN:
                print(f"鼠标点击坐标: ({X}, {Y})")
                global mouseX, mouseY
                mouseX = X
                mouseY = Y

                # 解除回调
                cv2.setMouseCallback("Select Pad Template", lambda *args: None)  # 解除回调

        # 设置鼠标回调
        cv2.setMouseCallback("Select Pad Template", mouse_callback)

        # 使用一个小的等待时间，避免等待太长时间
        while True:
            # 以 1ms 的延迟等待键盘事件或鼠标点击
            key = cv2.waitKey(1)  # 不阻塞，避免长时间卡住
            if mouseX != 0 and mouseY != 0:  # 判断是否有鼠标点击
                break
            if key == 27:  # 监听 ESC 键退出
                print("用户按下 ESC 键退出。")
                cv2.destroyWindow("Select Pad Template")
                return None

        # 进行模板匹配
        load_templates()
        with open('Paddia.txt', 'w') as f:
            f.write(f"{0},{0}")
        point = match_device_templates(screenshot)
        x_dia = mouseX - point[0][0]
        y_dia = mouseY + point[0][1]

        cv2.destroyWindow("Select Pad Template")

        # 保存偏移量
        with open('Paddia.txt', 'w') as f:
            f.write(f"{x_dia},{y_dia}")
        print(f"偏移量已保存: x_dia={x_dia}, y_dia={y_dia}")


    def CalIU(self):

        """
            Function:
              用于测量探针的IU性能，这里就是直接执行用户自己输入的JiaoBen文件
              执行后，强行将探针抬起来了，防止出现损坏
            Args:
              none
            Return:
              none
        """
        try:
            self.save_image()
            run_script = self.lineEdit_Scripts.text()
            if run_script == '':
                run_script = "./jiaoben.py"

            save_script = self.lineEdit_SaveResult.text()
            if save_script == '':
                save_script = 'D:\\lzg\\data\\' + time.strftime("save_%Y-%m-%d_%H-%M-%S") + '\\IV\\'

            result = subprocess.run(
                [sys.executable, run_script, save_script],
                capture_output=True,
                text=True,
                check=True,  # 如果返回非零会抛出异常
                encoding='utf-8',  # 明确指定编码
            )
            logger.log(result.stdout)
            logger.log("当前时刻测量成功")

        except Exception as e:
            logger.log(f"执行过程中发生错误: {str(e)}")

    # def update_log_display(self):
    #     '''
    #         Function:
    #             用于和定时器进行绑定，更新日志
    #         Args:
    #             none
    #         Return:
    #             none
    #     '''
    #     try:
    #         with open(self.log_file, 'r') as f:
    #             lines = f.readlines()
    #             # 取最后三行日志
    #             last_lines = lines[-10:]
    #             # 更新日志显示内容
    #             self.plainTextEdit_log.setPlainText("".join(last_lines))
    #     except FileNotFoundError:
    #         self.plainTextEdit_log.setPlainText("No logs available.")

    def update_log_display(self):
        '''
        Function:
            用于和定时器进行绑定，更新日志显示
        Args:
            none
        Return:
            none
        '''
        try:
            # 获取当天日志内容
            log_content = logger.get_today_logs()

            # 分割日志行并反转顺序（最新的在最前面）
            lines = log_content.split('\n')
            reversed_lines = lines[::-1]  # 反转列表

            # 取前10行（最新的10条）
            first_lines = reversed_lines[:10] if len(reversed_lines) >= 10 else reversed_lines

            # 更新日志显示内容
            self.plainTextEdit_log.setPlainText("\n".join(first_lines))

        except Exception as e:
            self.plainTextEdit_log.setPlainText(f"Log display error: {str(e)}")



    def checkbox_template_changed(self,state):
        # 根据复选框的状态更新标志位
        if state == Qt.Checked:
            self.DeviceTemplate_view = True
        else:
            self.DeviceTemplate_view = False

    def checkbox_state_changed(self, state):
        # 根据复选框的状态更新标志位
        if state == Qt.Checked:
            self.align_allowed = True
        else:
            self.align_allowed = False

    def checkbox_ElecNeedle_changed(self, Checkbox):
        # 根据复选框的状态更新标志位
        if Checkbox.isChecked:
            MainPage1.equipment = 0
            self.label_needle1.setText("探针位移")
        else:
            MainPage1.equipment = 1
            self.label_needle1.setText("光纤位移")

    def checkbox_Light_changed(self, Checkbox):
        # 根据复选框的状态更新标志位
        if Checkbox.isChecked:
            MainPage1.equipment = 1
            self.label_needle1.setText("光纤位移")
        else:
            MainPage1.equipment = 0
            self.label_needle1.setText("探针位移")

    # 自动跟随函数
    def align_frame_with_probe(self):
        if not self.allow_alignment:  # 检查是否允许对齐
            return self.frame_resized

        # 新增线程状态检查（关键修改）
        if hasattr(self, '_align_thread_running') and self._align_thread_running:
            return self.frame_resized

        def align():
            self._align_thread_running = True  # 标记线程开始
            try:
                while self.align_allowed:
                    # 原对齐逻辑保持不变...
                    frame_center_x = self.frame_resized.shape[1] // 2
                    frame_center_y = self.frame_resized.shape[0] // 2

                    probe_x, probe_y = self.get_probe_position()
                    if probe_x is None:
                        print("模板匹配失败，请先进行模板匹配")
                        break

                    distance_x = frame_center_x - probe_x
                    distance_y = frame_center_y - probe_y
                    distance = np.sqrt(distance_x ** 2 + distance_y ** 2)

                    if distance < 5:
                        break

                    b = 1000
                    if distance_y < 0:
                        ReturnZauxdll(self.microY, self.microdown * abs(distance_y) / b)
                    elif distance_y > 0:
                        ReturnZauxdll(self.microY, self.microup * abs(distance_y) / b)
                    if distance_x < 0:
                        ReturnZauxdll(self.microX, self.microright * abs(distance_x) / b)
                    elif distance_x > 0:
                        ReturnZauxdll(self.microX, self.microleft * abs(distance_x) / b)

                    cv2.circle(self.frame_resized, (frame_center_x, frame_center_y), 5, (255, 0, 0), -1)
                    time.sleep(0.2)  # 建议添加小延迟防止CPU占用过高
            finally:
                self._align_thread_running = False  # 确保线程结束标记

        # 启动线程（保持原daemon=True设置）
        threading.Thread(target=align, daemon=True).start()
        return self.frame_resized

    # 获得探针位置
    def get_probe_position(self):
        global red_dot_x
        global red_dot_y
        return red_dot_x, red_dot_y

    # 显微镜移动函数
    def move_microscope_up(self):
        distance = self.get_distance(MainPage1.micro_distanceY, 0.5)
        threading.Thread(target=ReturnZauxdll, args=(self.microY, self.microup * distance)).start()

    def move_microscope_down(self):
        distance = self.get_distance(MainPage1.micro_distanceY, 0.5)
        threading.Thread(target=ReturnZauxdll, args=(self.microY, self.microdown * distance)).start()

    def move_microscope_left(self):
        distance = self.get_distance(MainPage1.micro_distanceX, 0.5)
        threading.Thread(target=ReturnZauxdll, args=(self.microX, self.microleft * distance)).start()

    def move_microscope_right(self):
        distance = self.get_distance(MainPage1.micro_distanceX, 0.5)
        threading.Thread(target=ReturnZauxdll, args=(self.microX, self.microright * distance)).start()

    def get_distance(self, input_distance, default_distance):
        try:
            return float(input_distance) if input_distance else default_distance
        except ValueError:
            return default_distance

    def move_probe_up(self):
        threading.Thread(target=WhileMove,
                         args=(0, MainPage1.equipment, MainPage1.needle_distanceY)).start()
        logger.log("探针往上移动了")

    def move_probe_down(self):
        threading.Thread(target=WhileMove,
                         args=(1, MainPage1.equipment, MainPage1.needle_distanceY)).start()
        logger.log("探针往下移动了")

    def move_probe_left(self):
        threading.Thread(target=WhileMove,
                         args=(2, MainPage1.equipment, MainPage1.needle_distanceX)).start()
        logger.log("探针往左移动了")

    def move_probe_right(self):
        threading.Thread(target=WhileMove,
                         args=(3, MainPage1.equipment, MainPage1.needle_distanceX)).start()
        logger.log("探针往右移动了")

    from PyQt5.QtWidgets import QMessageBox

    def update_needle_distanceX(self):
        try:
            input_value = float(self.lineEdit_needle1Xdistance.text())
            if input_value > 3000:
                QMessageBox.warning(
                    self,  # 父窗口
                    "输入超出范围",  # 窗口标题
                    "X 轴移动距离不能超过 3000！"  # 提示信息
                )
                # 可以在这里重置输入框的值（可选）
                self.lineEdit_needle1Xdistance.setText("3000")
            MainPage1.needle_distanceX = min(3000, input_value)
        except ValueError:
            QMessageBox.warning(
                self,
                "输入错误",
                "请输入有效的数字！"
            )

    def update_needle_distanceY(self):
        try:
            input_value = float(self.lineEdit_needle1Ydistance.text())
            if input_value > 3000:
                QMessageBox.warning(
                    self,
                    "输入超出范围",
                    "Y 轴移动距离不能超过 3000！"
                )
                self.lineEdit_needle1Ydistance.setText("3000")
            MainPage1.needle_distanceY = min(3000, input_value)
        except ValueError:
            QMessageBox.warning(
                self,
                "输入错误",
                "请输入有效的数字！"
            )

    def update_needle_distanceZ(self):
        try:
            input_value = float(self.lineEdit_needle1Zdistance.text())
            if input_value > 1000:
                QMessageBox.warning(
                    self,
                    "输入超出范围",
                    "Z 轴移动距离不能超过 1000！"
                )
                self.lineEdit_needle1Zdistance.setText("1000")
            MainPage1.needle_distanceZ = min(1000, input_value)
        except ValueError:
            QMessageBox.warning(
                self,
                "输入错误",
                "请输入有效的数字！"
            )

    def STOP_MOVE(self):
        MainPage1.stop_num = 1

        anc = NeedelConnectionThread.anc
        anc.write('[ch1:1]'.encode())
        anc.write('[cap:000nF]'.encode())
        anc.write('[volt:+000V] '.encode())
        anc.write('[freq:+00000Hz]'.encode())
        time.sleep(0.2)
        anc.write('[ch2:1]'.encode())
        anc.write('[cap:000nF]'.encode())
        anc.write('[volt:+000V] '.encode())
        anc.write('[freq:+00000Hz]'.encode())
        time.sleep(0.2)
        anc.write('[ch3:1]'.encode())
        anc.write('[cap:000nF]'.encode())
        anc.write('[volt:+000V] '.encode())
        anc.write('[freq:+00000Hz]'.encode())
        time.sleep(0.2)
        anc.write('[ch1:0]'.encode())
        anc.write('[ch2:0]'.encode())
        anc.write('[ch3:0]'.encode())
        time.sleep(0.2)

    def restart_program(self):
        python = sys.executable  # 当前 python 解释器路径
        os.execl(python, python, *sys.argv)  # 使用同样的参数重新执行该脚本

    # 鼠标点击运动
    def mousePressEvent(self, event):
        """
            Function:
                用户点击画面的一个位置，探针会移动到这个位置
            Args:
                鼠标左键点击事件
            Return:
                none
        """
        # 获取 label_video 在屏幕中的位置
        top_left_global = self.label_video.mapToGlobal(QtCore.QPoint(0, 0))

        # 获取鼠标点击位置的全局坐标
        global_point = event.globalPos()

        # 计算点击位置相对于 label_video 的位置
        relative_x = global_point.x() - top_left_global.x()
        relative_y = global_point.y() - top_left_global.y()

        # 获取视频的宽高
        video_width = self.frame_resized.shape[1]
        video_height = self.frame_resized.shape[0]

        # 设置目标坐标
        self.target_x = relative_x
        self.target_y = relative_y

        # 检查目标坐标是否在有效区域内
        if self.board_width / 2 <= self.target_x <= video_width - self.board_width / 2 and self.board_height / 2 <= self.target_y <= video_height - self.board_height / 2:
            if event.button() == QtCore.Qt.LeftButton:
                confirm = QMessageBox.question(self, '确认操作', '您确定要移动探针吗?',
                                               QMessageBox.Yes | QMessageBox.No)
                if confirm == QMessageBox.Yes:
                    logger.log("执行了一次探针鼠标点击运动")
                    threading.Thread(target=self.move_probe_to_target, args=(self.target_x, self.target_y)).start()
                    self.indicator.setStyleSheet(MainPage1.get_stylesheet(False))
        elif 0 <= self.target_x <= video_width and 0 <= self.target_y <= video_height:
            QMessageBox.warning(self, '提示', '请在视频有效区域内点击！', QMessageBox.Ok)
            return

    # 计算距离并移动探针
    def move_probe_to_target(self, target_x, target_y):
        distance_weight = 50 #低温50，常温1
        self.allow_alignment = False  # 禁用对齐
        self.indicator.setStyleSheet(MainPage1.get_stylesheet(True))
        probe_x, probe_y = self.get_probe_position()
        distance = np.sqrt((target_x - probe_x) ** 2) *distance_weight
        while distance>=3:
            if StopClass.stop_num == 1:
                break
            if probe_x is None:
                logger.log("模板匹配失败，请先进行模板匹配")
                break
            if target_x < probe_x:
                ReturnNeedleMove(self.needleuleft, distance, self.indicator, True, False, MainPage1.equipment)
            elif target_x > probe_x:
                ReturnNeedleMove(self.needleright, distance, self.indicator, True, False, MainPage1.equipment)
            # 低温情况下time.sleep应该是0.5，常温情况是0.1
            time.sleep(0.5)
            probe_x, probe_y = self.get_probe_position()
            distance = np.sqrt((target_x - probe_x) ** 2)*distance_weight

        distance = np.sqrt((target_y - probe_y) ** 2)*distance_weight
        while distance>=3:
            if StopClass.stop_num == 1:
                break
            if probe_y is None:
                logger.log("模板匹配失败，请先进行模板匹配")
                break
            if target_y < probe_y:
                ReturnNeedleMove(self.needleup, distance, self.indicator, True, False, MainPage1.equipment)
            elif target_y > probe_y:
                ReturnNeedleMove(self.needledown, distance, self.indicator, True, False, MainPage1.equipment)
            # 低温情况下time.sleep应该是0.5，常温情况是0.1
            time.sleep(0.5)
            probe_x, probe_y = self.get_probe_position()
            distance = np.sqrt((target_y - probe_y) ** 2)*distance_weight



        self.allow_alignment = True  # 重新允许对齐
        self.indicator.setStyleSheet(MainPage1.get_stylesheet(False))
        MainPage1.stop_num = 0

    # 928更新电压的函数
    def update_voltage(self):
        """
            Function:
                用于和按钮事件绑定，更新赋予探针的电压
            Args:
                none
            Return:
                none
        """
        # sim928_2 = SIM928(5, 'GPIB4::2::INSTR')
        keithley = SIM928ConnectionThread.anc
        if keithley is None:
            print("keithley未正常连接")
        else:
            try:
                voltage_input = 0.1 if not self.lineEdit_SIM928.text() else float(self.lineEdit_SIM928.text())
            except ValueError:
                voltage_input = 0.1
                print("输入的不是有效数字，已使用默认值 0.1")
            try:
                keithley.use_rear_terminals  # 使用仪器前面端子
                keithley.wires
                keithley.apply_voltage()  # 设置为电压源
                keithley.compliance_current = 0.1  # 设置合规电流
                keithley.auto_range_source()
                keithley.measure_current()  # 设置为测量电流
                keithley.enable_source()  # 打开源表
                keithley.source_voltage = voltage_input
                time.sleep(0.1)
            except (AttributeError, ValueError):
                print("keithley未正常连接")

    def Pushing(self):
        if SIM928ConnectionThread.anc is None or not self.lineEdit_SIM928.text():
            logger.log("警告：anc 是 None，无法执行 Pushing 操作")

        WhileMove(4, MainPage1.equipment, MainPage1.needle_distanceZ)
        logger.log("探针下压了")

    def Pulling(self):
        if SIM928ConnectionThread.anc is None or not self.lineEdit_SIM928.text():
            logger.log("警告：anc 是 None，无法执行 Pulling 操作")

        # 常温下min的最大值是1000，低温下min的最大值是5000
        WhileMove(5, MainPage1.equipment, MainPage1.needle_distanceZ)
        logger.log("探针抬升了")


def Color_numpy(data, nWidth, nHeight):
    data_ = np.frombuffer(data, count=int(nWidth * nHeight * 3), dtype=np.uint8, offset=0)
    data_r = data_[0:nWidth * nHeight * 3:3]
    data_g = data_[1:nWidth * nHeight * 3:3]
    data_b = data_[2:nWidth * nHeight * 3:3]

    data_r_arr = data_r.reshape(nHeight, nWidth)
    data_g_arr = data_g.reshape(nHeight, nWidth)
    data_b_arr = data_b.reshape(nHeight, nWidth)
    numArray = np.zeros([nHeight, nWidth, 3], "uint8")

    numArray[:, :, 0] = data_r_arr
    numArray[:, :, 1] = data_g_arr
    numArray[:, :, 2] = data_b_arr
    return numArray