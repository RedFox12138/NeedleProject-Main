import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

import matplotlib
import numpy as np
from PyQt5.QtCore import QTimer
from matplotlib import pyplot as plt, animation
from matplotlib.widgets import Button


#
from QTneedle.QTneedle.Position import getPosition, move_to_target, move_to_Z
from SerialPage import SIM928ConnectionThread

from StopClass import StopClass

custom_lib_path = "c:\\users\\administrator\\appdata\\local\\programs\\python\\python37\\lib\\site-packages"
# 将路径添加到 sys.path
if custom_lib_path not in sys.path:
    sys.path.append(custom_lib_path)
import threading
import time
from PyQt5.QtWidgets import QMainWindow
from QTneedle.QTneedle.SerialLock import SerialLock
from QTneedle.QTneedle.demo import Ui_MainWindow
matplotlib.use('TkAgg')

# 设置中文字体
plt.rcParams['font.family'] = 'SimHei'
# 解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False
# 全局变量，用于控制测试的启动和停止
test_event = threading.Event()


class locationClass(QMainWindow, Ui_MainWindow):
    locationX = 0
    locationY = 0
    locationZ = 0
    def __init__(self,lineEdit_Xlocation,lineEdit_Ylocation,lineEdit_Zlocation,
                 lineEdit_Location1,lineEdit_Location2,lineEdit_Location3,
                 Button_Location1,Button_Location2,Button_Location3,
                 lineEdit_row,lineEdit_col,Button_CreateMap,mainpage1,
                 Button_ContinueTest,Button_StopTest,
                 lineEdit_Pushlocation, lineEdit_Pulllocation,
                 Button_PushLocation, Button_PullLocation,
                 Button_PushBack, Button_PullBack,lineEdit_Scripts,lineEdit_SaveResult
    ):
        super().__init__()
        self.lineEdit_SaveResult = lineEdit_SaveResult
        self.lineEdit_Scripts = lineEdit_Scripts
        self.device_positions = []
        self.ax = None
        self.fig = None
        self.mainpage1 = mainpage1
        self.lineEdit_Xlocation = lineEdit_Xlocation
        self.lineEdit_Ylocation = lineEdit_Ylocation
        self.lineEdit_Zlocation = lineEdit_Zlocation
        self.lineEdit_row = lineEdit_row
        self.lineEdit_col = lineEdit_col

        self.lineEdit_Pushlocation = lineEdit_Pushlocation
        self.lineEdit_Pulllocation = lineEdit_Pulllocation


        self.location1 = 0
        self.location2 = 0
        self.location3 = 0
        self.Zlocation1 = 0
        self.Zlocation2 = 0

        self.lineEdit_Location1 = lineEdit_Location1
        self.lineEdit_Location2 = lineEdit_Location2
        self.lineEdit_Location3 = lineEdit_Location3

        # self.lineEdit_Location1.setText("0")
        # self.lineEdit_Location2.setText("0")
        # self.lineEdit_Location3.setText("0")

        Button_Location1.clicked.connect(lambda: threading.Thread(target=self.ConfirmPosition, args=(1,)).start())
        Button_Location2.clicked.connect(lambda: threading.Thread(target=self.ConfirmPosition, args=(2,)).start())
        Button_Location3.clicked.connect(lambda: threading.Thread(target=self.ConfirmPosition, args=(3,)).start())

        Button_PushLocation.clicked.connect(lambda: threading.Thread(target=self.ZConfirmPosition, args=(1,)).start())
        Button_PullLocation.clicked.connect(lambda: threading.Thread(target=self.ZConfirmPosition, args=(2,)).start())

        Button_CreateMap.clicked.connect(lambda: threading.Thread(target=self.CreateMap).start())

        Button_ContinueTest.clicked.connect(lambda: threading.Thread(target=self.continue_test).start())
        Button_StopTest.clicked.connect(lambda: threading.Thread(target=self.stop_test).start())

        Button_PushBack.clicked.connect(lambda: threading.Thread(target=self.PushBack).start())
        Button_PullBack.clicked.connect(lambda: threading.Thread(target=self.PullBack).start())

        self.log_timer = QTimer(self)
        self.log_timer.timeout.connect(self.update_location_display)
        self.log_timer.start(500)  # 每秒更新一次

        # 开始测试按钮 从头开始自动化测试
        # 创建按钮并调整布局

    def PushBack(self,flag=True):
        move_to_Z(self.Zlocation1,flag)
        locationClass.locationX, locationClass.locationY, locationClass.locationZ = getPosition()

    def PullBack(self):
        move_to_Z(self.Zlocation2)
        locationClass.locationX, locationClass.locationY, locationClass.locationZ = getPosition()

    def update_location_display(self):
        self.lineEdit_Xlocation.setText(str(locationClass.locationX))
        self.lineEdit_Ylocation.setText(str(locationClass.locationY))
        self.lineEdit_Zlocation.setText(str(locationClass.locationZ))

    def ConfirmPosition(self,flag):
        with SerialLock.serial_lock:
            locationClass.locationX,locationClass.locationY,locationClass.locationZ = getPosition()
        if flag == 1:
            self.location1 = (locationClass.locationX,locationClass.locationY)
            self.lineEdit_Location1.setText(str(self.location1))
        if flag == 2:
            self.location2 = (locationClass.locationX, locationClass.locationY)
            self.lineEdit_Location2.setText(str(self.location2))
        if flag == 3:
            self.location3 = (locationClass.locationX, locationClass.locationY)
            self.lineEdit_Location3.setText(str(self.location3))

    def ZConfirmPosition(self,flag):
        with SerialLock.serial_lock:
            _, _, locationClass.locationZ = getPosition()
        if flag == 1:
            self.Zlocation1 = locationClass.locationZ - 0.01
            self.lineEdit_Pushlocation.setText(str(self.Zlocation1))
        if flag == 2:
            self.Zlocation2 = locationClass.locationZ + 0.01
            self.lineEdit_Pulllocation.setText(str(self.Zlocation2))


    def CreateMap(self):



        # 关闭之前打开的图形窗口（如果存在）
        if hasattr(self, 'fig') and self.fig is not None:
            plt.close(self.fig)
            self.fig = None  # 显式释放资源


        # 用户输入的参数
        top_left = (-0.3835, -2.2729)
        top_right = (-0.6593, -2.2734)
        bottom_right = (-0.6587, -2.4062)
        row = 2
        col = 2
        #
        # row = int(self.lineEdit_row.text())
        # col = int(self.lineEdit_col.text())
        #
        # if(row==0 or col==0 or self.location1==0 or self.location2==0 or self.location3==0):
        #     print("参数配置未完成，无法生成MAP")
        # else:
        #     self.device_positions = self.calculate_device_positions(self.location1,self.location2,self.location3,row,col)

        self.device_positions = self.calculate_device_positions(top_left, top_right, bottom_right, row, col)

        # 创建新的图形和坐标轴
        self.fig, self.ax = plt.subplots()

        # 修改后（将标签移到坐标轴外）
        info_text = self.ax.text(
            -0.36, 1.05,  # x负方向偏移25%，y正方向偏移5%
            'Status: Ready\n(0.00, 0.00)',
            transform=self.ax.transAxes,  # 保持坐标轴坐标系
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
            fontsize=9,
            clip_on=False  # 关键！关闭裁剪限制
        )
        self.ax.set_xlim(4, -4)
        self.ax.set_ylim(-4, 4)
        self.ax.set_aspect('equal')

        # 绘制设备点
        device_scatter = self.ax.scatter(
            [pos[0] for pos in self.device_positions],
            [pos[1] for pos in self.device_positions],
            color='blue', label='设备'
        )

        # 绘制探针点
        probe_point, = self.ax.plot([], [], 'ro', label='探针')

        # 使用动画API替代线程
        def animate(_):
            try:
                # 更新探针位置
                probe_point.set_data([locationClass.locationX], [locationClass.locationY])

                # 更新信息文本
                info_text.set_text('Time: %s\nX: %.4f\nY: %.4f' % (
                    datetime.now().strftime("%H:%M:%S"),
                    locationClass.locationX,
                    locationClass.locationY
                ))

                # 请求重绘（线程安全方式）
                self.fig.canvas.draw_idle()
            except Exception as e:
                print(f"更新异常: {e}")
                return

        # 创建动画对象
        self.ani = animation.FuncAnimation(
            self.fig,
            animate,
            interval=2000,  # 2秒间隔
            cache_frame_data=False
        )
        # 绑定鼠标点击事件
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)

        plt.show()

    # def start_test(self):
    #     if not test_event.is_set():
    #         move_thread = threading.Thread(target=self.continue_test, daemon=True)
    #         move_thread.start()

    # 遍历设备位置，依次移动探针 从头开始测试所有的探针
    def move_to_all_targets(self,start_index=0):
        test_event.set()
        try:
            for i in range(start_index, len(self.device_positions)):
                if not test_event.is_set() or StopClass.stop_num==1:
                    StopClass.stop_num=0
                    break
                target_x, target_y = self.device_positions[i]
                print(f'移动到目标点: x={target_x}, y={target_y}')
                move_to_target(target_x, target_y)
                self.mainpage1.match_and_move()
                locationClass.locationX, locationClass.locationY,_ = getPosition()
                time.sleep(1)  # 等待 1 秒，确保探针稳定
                keithley = SIM928ConnectionThread.anc
                keithley.use_rear_terminals  # 使用仪器前面端子
                keithley.wires
                keithley.apply_voltage()  # 设置为电压源
                keithley.compliance_current = 0.1  # 设置合规电流
                keithley.auto_range_source()
                keithley.measure_current()  # 设置为测量电流
                keithley.enable_source()  # 打开源表
                keithley.source_voltage = 0.1

                # keithley = SIM928ConnectionThread.anc
                self.PushBack(True)
                time.sleep(0.5)  # 等待 1 秒，确保探针稳定
                # try:
                #     current = keithley.current
                # except Exception as e:
                #     current = 10e-11
                current = keithley.current
                print("按压完成后的电流是",current)
                if current >= 9e-10:
                    #执行IU计算
                    run_script = self.lineEdit_Scripts.text()
                    if (run_script == ''):
                        run_script = "./jiaoben.py"

                    save_script = self.lineEdit_SaveResult.text()
                    if (save_script == ''):
                        save_script = 'D:\\lzg\\data\\' + time.strftime("save_%Y-%m-%d_%H-%M-%S") + '\\IV\\'

                    result = subprocess.run(
                        [sys.executable, run_script, save_script],
                        capture_output=True,
                        text=True,
                        check=True,  # 如果返回非零会抛出异常
                        encoding='utf-8',  # 明确指定编码
                    )
                    print(result.stdout)
                self.PullBack()



        except Exception as e:
            print(f"移动线程出现异常: {e}")
        finally:
            test_event.clear()

    def continue_test(self):
        if not test_event.is_set():
            with SerialLock.serial_lock:
                current_x, current_y,_ = getPosition()
        nearest_index = self.find_nearest_index(current_x, current_y)
        start_index = nearest_index  if nearest_index < len(self.device_positions) else 0
        move_thread = threading.Thread(target=self.move_to_all_targets, args=(start_index,), daemon=True)
        move_thread.start()

    def stop_test(self):
        test_event.clear()
        print(f"当前一个芯片测量结束后，会自动终止测试")

    # def calculate_device_positions(self,top_left, top_right, bottom_right, rows, cols):
    #     x = np.linspace(top_left[0], top_right[0], cols)
    #     y = np.linspace(top_left[1], bottom_right[1], rows)
    #     xx, yy = np.meshgrid(x, y)
    #     return list(zip(xx.flatten(), yy.flatten()))

    def calculate_device_positions(self, top_left, top_right, bottom_right, rows, cols):
        x = np.linspace(top_left[0], top_right[0], cols)
        y = np.linspace(top_left[1], bottom_right[1], rows)
        xx, yy = np.meshgrid(x, y)

        # 转置网格点矩阵，然后展平，实现竖向编号
        return list(zip(xx.T.flatten(), yy.T.flatten()))


    # 鼠标点击事件处理函数
    def on_click(self,event):
        click_x, click_y = event.xdata, event.ydata
        nearest_index = self.find_nearest_index(click_x, click_y)
        target_x, target_y = self.device_positions[nearest_index]
        with ThreadPoolExecutor() as executor:
            future = executor.submit(move_to_target, target_x, target_y)
            locationClass.locationX,locationClass.locationY = future.result()  # 获取运行结果
            future.add_done_callback(self.on_move_complete)


    def on_move_complete(self,future):
        # 当 move_to_target 完成后执行的回调函数
        locationClass.locationX, locationClass.locationY = future.result()
        self.mainpage1.match_and_move()

    # 找到距离当前位置最近的点的索引
    def find_nearest_index(self,current_x, current_y):
        distances = [np.sqrt((current_x - pos[0])**2 + (current_y - pos[1])**2) for pos in self.device_positions]
        nearest_index = np.argmin(distances)
        return nearest_index


