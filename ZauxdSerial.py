import serial.tools.list_ports
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QPushButton, QLabel
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
import zauxdllPython  # 假设你使用的是 zauxdllPython 进行串口连接
from ANC300 import Positioner
from SRS_SIM928 import SIM928
from SRS_SIM970 import SRSSIM970
from ZauxdllTest import GBIOConnect


#位移器的串口连接
class SerialConnectionThread(QThread):
    # 定义信号，用来通知主界面连接成功或失败
    connected = pyqtSignal(bool, str)
    zaux = None

    def __init__(self, port_number):
        super().__init__()
        self.port_number = port_number

    def run(self):
        """ 运行连接操作 """
        try:
            SerialConnectionThread.zaux = zauxdllPython.ZMCWrapper()
            SerialConnectionThread.zaux.connectcom(self.port_number)
            SerialConnectionThread.zaux.set_atype(0, 1)
            SerialConnectionThread.zaux.set_units(0, 10000)
            SerialConnectionThread.zaux.set_accel(0, 1000)
            SerialConnectionThread.zaux.set_decel(0, 10)
            SerialConnectionThread.zaux.set_speed(0, 1000)
            SerialConnectionThread.zaux.get_atype(0)
            SerialConnectionThread.zaux.get_untis(0)
            SerialConnectionThread.zaux.get_accel(0)
            SerialConnectionThread.zaux.get_decel(0)
            SerialConnectionThread.zaux.get_speed(0)
            self.connected.emit(True, f"连接成功，端口 {self.port_number}")
        except Exception as e:
            self.connected.emit(False, f"连接失败: {str(e)}")


class NeedelConnectionThread(QThread):
    # 定义信号，用来通知主界面连接成功或失败
    connected = pyqtSignal(bool, str)
    anc = None
    def __init__(self, port_number):
        super().__init__()
        self.port_number = port_number

    def run(self):
        """ 运行连接操作 """
        try:
            port_name = 'ASRL'+str(self.port_number)+'::INSTR'
            NeedelConnectionThread.anc = Positioner(port_name)  # anc300地址
            # 定义位移函数=============================================================================
            ax = {'x': 1, 'y': 2, 'z': 3, 'x2': 4, 'y2': 5, 'z2': 6}
            for AID in sorted(ax.keys()):
                NeedelConnectionThread.anc.setf(ax[AID], 100)  # 加速度
                NeedelConnectionThread.anc.setv(ax[AID], 100)

            # NeedelConnectionThread.anc.setm(ax['x'], 'stp')
            # NeedelConnectionThread.anc.stepu(ax['x'], 0.1)
            # # t = math.ceil(distance / 300) + 1
            # time.sleep(0.1)  # x2+
            self.connected.emit(True, f"连接成功，端口 {self.port_number}")
        except Exception as e:
            self.connected.emit(False, f"连接失败: {str(e)}")


class SIM928ConnectionThread(QThread):
    # 定义信号，用来通知主界面连接成功或失败
    connected = pyqtSignal(bool, str)
    anc = None
    def __init__(self, port_number,GBIO_number):
        super().__init__()
        self.port_number = port_number
        self.GBIO_number = GBIO_number
    def run(self):
        """ 运行连接操作 """
        try:
            SIM928ConnectionThread.anc = SIM928(self.port_number, self.GBIO_number)
            self.connected.emit(True, f"连接成功，端口 {self.GBIO_number}")
        except Exception as e:
            self.connected.emit(False, f"连接失败: {str(e)}")

class SIM970ConnectionThread(QThread):
    # 定义信号，用来通知主界面连接成功或失败
    connected = pyqtSignal(bool, str)
    anc = None
    def __init__(self, port_number,GBIO_number):
        super().__init__()
        self.port_number = port_number
        self.GBIO_number = GBIO_number
    def run(self):
        """ 运行连接操作 """
        try:
            SIM970ConnectionThread.anc = SRSSIM970(self.port_number, self.GBIO_number)
            self.connected.emit(True, f"连接成功，端口 {self.GBIO_number}")
        except Exception as e:
            self.connected.emit(False, f"连接失败: {str(e)}")

class SerialConnectionPage(QWidget):
    def __init__(self):
        super().__init__()

        # 创建串口连接页面的布局
        layout = QVBoxLayout(self)

        # 显微镜位移器
        # 创建串口选择标签
        self.port_label = QLabel('请选择显微镜串口:')
        layout.addWidget(self.port_label)

        # 创建串口选择下拉框
        self.port_combo = QComboBox()
        self.update_serial_ports(self.port_combo)  # 更新可用串口
        layout.addWidget(self.port_combo)

        # 创建连接按钮
        self.connect_button = QPushButton('连接')
        self.connect_button.clicked.connect(lambda: self.connect_to_serial('micro'))
        layout.addWidget(self.connect_button)

        # 创建连接状态指示灯
        self.status_led = QLabel('连接状态: 未连接')
        self.status_led.setStyleSheet("color: red; font-size: 16px;")
        # 创建断开连接按钮
        self.disconnect_button = QPushButton('断开连接')
        self.disconnect_button.setEnabled(False)  # 初始为禁用
        self.disconnect_button.clicked.connect(lambda: self.disconnect_from_serial("micro",self.status_led,self.connect_button,self.disconnect_button))
        layout.addWidget(self.disconnect_button)


        layout.addWidget(self.status_led)


        #探针位移器
        self.needle_port_label = QLabel('请选择探针串口:')
        layout.addWidget(self.needle_port_label)

        # 创建串口选择下拉框
        self.needle_port_combo = QComboBox()
        self.update_serial_ports(self.needle_port_combo)  # 更新可用串口
        layout.addWidget(self.needle_port_combo)

        # 创建连接按钮
        self.needle_connect_button = QPushButton('连接')
        self.needle_connect_button.clicked.connect(lambda: self.connect_to_serial('needle'))
        layout.addWidget(self.needle_connect_button)

        # 创建连接状态指示灯
        self.needle_status_led = QLabel('连接状态: 未连接')
        self.needle_status_led.setStyleSheet("color: red; font-size: 16px;")
        self.needle_disconnect_button = QPushButton('断开连接')
        self.needle_disconnect_button.setEnabled(False)  # 初始为禁用
        self.needle_disconnect_button.clicked.connect(lambda: self.disconnect_from_serial("needle",self.needle_status_led,
                                                                                  self.needle_connect_button,self.needle_disconnect_button))
        layout.addWidget(self.needle_disconnect_button)


        layout.addWidget(self.needle_status_led)



        # 扫描GBIO的设备
        self.GBIO_connect_button = QPushButton('扫描所有GBIO设备')

        layout.addWidget(self.GBIO_connect_button)

        # SIM928
        self.SIM928_port_label = QLabel('请选择SIM928串口:')
        layout.addWidget(self.SIM928_port_label)

        # 创建串口选择下拉框
        self.SIM928_GBIO_combo = QComboBox()
        self.update_GBIO_ports(self.SIM928_GBIO_combo)  # 更新可用串口
        layout.addWidget(self.SIM928_GBIO_combo)

        self.SIM928_port_combo = QComboBox()
        for num in range(1,11):
            self.SIM928_port_combo.addItem(str(num))  # 添加串口设备名称
        layout.addWidget(self.SIM928_port_combo)

        # 创建连接按钮
        self.SIM928_connect_button = QPushButton('连接')
        self.SIM928_connect_button.clicked.connect(lambda: self.connect_to_serial('SIM928'))
        layout.addWidget(self.SIM928_connect_button)
        # 创建连接状态指示灯
        self.SIM928_status_led = QLabel('连接状态: 未连接')
        self.SIM928_status_led.setStyleSheet("color: red; font-size: 16px;")
        self.SIM928_disconnect_button = QPushButton('断开连接')
        self.SIM928_disconnect_button.setEnabled(False)  # 初始为禁用
        self.SIM928_disconnect_button.clicked.connect(lambda: self.disconnect_from_serial("SIM928",self.SIM928_status_led,
                                                                                  self.SIM928_connect_button,self.SIM928_disconnect_button))
        layout.addWidget(self.SIM928_disconnect_button)


        layout.addWidget(self.SIM928_status_led)

        # SIM970
        self.SIM970_port_label = QLabel('请选择SIM970串口:')
        layout.addWidget(self.SIM970_port_label)

        # 创建串口选择下拉框
        self.SIM970_GBIO_combo = QComboBox()
        self.update_GBIO_ports(self.SIM970_GBIO_combo)  # 更新可用串口
        layout.addWidget(self.SIM970_GBIO_combo)

        self.SIM970_port_combo = QComboBox()
        for num in range(1, 11):
            self.SIM970_port_combo.addItem(str(num))  # 添加串口设备名称
        layout.addWidget(self.SIM970_port_combo)

        # 创建连接按钮
        self.SIM970_connect_button = QPushButton('连接')
        self.SIM970_connect_button.clicked.connect(lambda: self.connect_to_serial('SIM970'))
        layout.addWidget(self.SIM970_connect_button)
        # 创建连接状态指示灯
        self.SIM970_status_led = QLabel('连接状态: 未连接')
        self.SIM970_status_led.setStyleSheet("color: red; font-size: 16px;")
        self.SIM970_disconnect_button = QPushButton('断开连接')
        self.SIM970_disconnect_button.setEnabled(False)  # 初始为禁用
        self.SIM970_disconnect_button.clicked.connect(lambda: self.disconnect_from_serial("SIM970",self.SIM970_status_led,
                                                                                  self.SIM970_connect_button,self.SIM970_disconnect_button))
        layout.addWidget(self.SIM970_disconnect_button)
        layout.addWidget(self.SIM970_status_led)

        self.GBIO_connect_button.clicked.connect(
            self.GBIO_clicked
        )

        # 设置布局
        self.setLayout(layout)

        # 初始化串口连接对象
        self.zaux = None
        self.connection_thread = None
        # 初始化连接超时计时器
        self.timer = QTimer(self)
        self.timer.setInterval(2000)  # 设置超时时间为2秒
        self.timer.timeout.connect(self.connection_timeout)

    def GBIO_clicked(self):
        GBIOConnect()  # 先执行
        self.update_GBIO_ports(self.SIM928_GBIO_combo)  # 再执行
        self.update_GBIO_ports(self.SIM970_GBIO_combo)  # 最后执行


    def update_serial_ports(self,port_combo):
        """ 获取系统中所有可用的串口，并更新到下拉框中 """
        ports = serial.tools.list_ports.comports()
        port_combo.clear()  # 清空现有串口列表
        for port in ports:
            port_combo.addItem(port.device)  # 添加串口设备名称

    def update_GBIO_ports(self,GBIO_combo):
        """ 获取系统中所有可用的串口，并更新到下拉框中 """
        GBIOs = GBIOConnect.connected_gpib_devices
        GBIOs.append("default")
        GBIO_combo.clear()
        for GBIO in GBIOs:
            GBIO_combo.addItem(GBIO)  # 添加串口设备名称


    def connect_to_serial(self,flag):
        """ 连接到选中的串口 """
        # 获取选择的串口号
        selected_port = self.port_combo.currentText()
        if not selected_port:
            self.status_led.setText('连接状态: 无串口可用')
            self.status_led.setStyleSheet("color: red; font-size: 16px;")
            return

        needle_selected_port = self.needle_port_combo.currentText()
        if not needle_selected_port:
            self.needle_status_led.setText('连接状态: 无串口可用')
            self.needle_status_led.setStyleSheet("color: red; font-size: 16px;")
            return

        SIM928_selected_GBIO = self.SIM928_GBIO_combo.currentText()
        SIM928_selected_port = self.SIM928_port_combo.currentText()
        if not SIM928_selected_GBIO or not SIM928_selected_port:
            self.SIM928_status_led.setText('连接状态: 无串口可用')
            self.SIM928_status_led.setStyleSheet("color: red; font-size: 16px;")
            return

        SIM970_selected_GBIO = self.SIM970_GBIO_combo.currentText()
        SIM970_selected_port = self.SIM970_port_combo.currentText()
        if not SIM970_selected_GBIO or not SIM970_selected_port:
            self.SIM970_status_led.setText('连接状态: 无串口可用')
            self.SIM970_status_led.setStyleSheet("color: red; font-size: 16px;")
            return

        # 启动超时计时器
        self.timer.start()

        # 启动连接线程
        port_number = int(selected_port[-1])  # 假设串口为 COMx 格式，取 x
        needle_prot_number = int(needle_selected_port[-1])
        SIM928_GBIO_number = SIM928_selected_GBIO
        SIM928_prot_number = int(SIM928_selected_port[-1])
        SIM970_GBIO_number = SIM970_selected_GBIO
        SIM970_prot_number = int(SIM970_selected_port[-1])

        if flag== "micro":
            self.connection_thread = SerialConnectionThread(port_number)
            self.connection_thread.connected.connect(self.handle_connection_result)
            self.connection_thread.start()
            self.connect_button.setEnabled(False)
            self.disconnect_button.setEnabled(False)
        elif flag== "needle":
            self.connection_thread = NeedelConnectionThread(needle_prot_number)
            self.connection_thread.connected.connect(self.needle_handle_connection_result)
            self.connection_thread.start()
            self.needle_connect_button.setEnabled(False)
            self.needle_disconnect_button.setEnabled(False)
        elif flag== "SIM928":
            self.connection_thread = SIM928ConnectionThread(SIM928_prot_number,SIM928_GBIO_number)
            self.connection_thread.connected.connect(self.SIM928_handle_connection_result)
            self.connection_thread.start()
            self.SIM928_connect_button.setEnabled(False)
            self.SIM928_disconnect_button.setEnabled(False)
        elif flag== "SIM970":
            self.connection_thread = SIM970ConnectionThread(SIM970_prot_number, SIM970_GBIO_number)
            self.connection_thread.connected.connect(self.SIM970_handle_connection_result)
            self.connection_thread.start()
            self.SIM970_connect_button.setEnabled(False)
            self.SIM970_disconnect_button.setEnabled(False)


    def connection_timeout(self):
        """ 超时处理：2秒内没有连接成功，判定为连接失败 """
        if self.connection_thread and self.connection_thread.isRunning():
            self.status_led.setText('连接状态: 连接超时，请检查串口')
            self.status_led.setStyleSheet("color: red; font-size: 16px;")
            self.timer.stop()  # 停止计时器
            self.connect_button.setEnabled(True)  # 启用连接按钮
            self.disconnect_button.setEnabled(False)  # 禁用断开连接按钮

    def handle_connection_result(self, success, message):
        """ 处理连接成功或失败的信号 """
        if success:
            self.status_led.setText(f'连接状态: {message}')
            self.status_led.setStyleSheet("color: green; font-size: 16px;")
            self.connect_button.setEnabled(False)  # 禁用连接按钮
            self.disconnect_button.setEnabled(True)  # 启用断开连接按钮
        else:
            self.status_led.setText(f'连接状态: {message}')
            self.status_led.setStyleSheet("color: red; font-size: 16px;")
            self.connect_button.setEnabled(True)  # 启用连接按钮
            self.disconnect_button.setEnabled(False)  # 禁用断开连接按钮

        self.timer.stop()  # 停止计时器

    def needle_handle_connection_result(self, success, message):
        """ 处理连接成功或失败的信号 """
        if success:
            self.needle_status_led.setText(f'连接状态: {message}')
            self.needle_status_led.setStyleSheet("color: green; font-size: 16px;")
            self.needle_connect_button.setEnabled(False)  # 禁用连接按钮
            self.needle_disconnect_button.setEnabled(True)  # 启用断开连接按钮
        else:
            self.needle_status_led.setText(f'连接状态: {message}')
            self.needle_status_led.setStyleSheet("color: red; font-size: 16px;")
            self.needle_connect_button.setEnabled(True)  # 启用连接按钮
            self.needle_disconnect_button.setEnabled(False)  # 禁用断开连接按钮
        self.timer.stop()  # 停止计时器

    def SIM928_handle_connection_result(self, success, message):
        """ 处理连接成功或失败的信号 """
        if success:
            self.SIM928_status_led.setText(f'连接状态: {message}')
            self.SIM928_status_led.setStyleSheet("color: green; font-size: 16px;")
            self.SIM928_connect_button.setEnabled(False)  # 禁用连接按钮
            self.SIM928_disconnect_button.setEnabled(True)  # 启用断开连接按钮
        else:
            self.SIM928_status_led.setText(f'连接状态: {message}')
            self.SIM928_status_led.setStyleSheet("color: red; font-size: 16px;")
            self.SIM928_connect_button.setEnabled(True)  # 启用连接按钮
            self.SIM928_disconnect_button.setEnabled(False)  # 禁用断开连接按钮
        self.timer.stop()  # 停止计时器

    def SIM970_handle_connection_result(self, success, message):
        """ 处理连接成功或失败的信号 """
        if success:
            self.SIM970_status_led.setText(f'连接状态: {message}')
            self.SIM970_status_led.setStyleSheet("color: green; font-size: 16px;")
            self.SIM970_connect_button.setEnabled(False)  # 禁用连接按钮
            self.SIM970_disconnect_button.setEnabled(True)  # 启用断开连接按钮
        else:
            self.SIM970_status_led.setText(f'连接状态: {message}')
            self.SIM970_status_led.setStyleSheet("color: red; font-size: 16px;")
            self.SIM970_connect_button.setEnabled(True)  # 启用连接按钮
            self.SIM970_disconnect_button.setEnabled(False)  # 禁用断开连接按钮
        self.timer.stop()  # 停止计时器

    def disconnect_from_serial(self,flag,status_led,connect_button,disconnect_button):
        """ 断开串口连接 """
        try:
            if flag == "micro":
                if SerialConnectionThread.zaux:
                    SerialConnectionThread.zaux.disconnect()
            elif flag == "needle":
                NeedelConnectionThread.anc = None
            elif flag == "SIM928":
                SIM928ConnectionThread.anc = None
            elif flag == "SIM970":
                SIM970ConnectionThread.anc.quit_vol()
                SIM970ConnectionThread.anc = None

            status_led.setText('连接状态: 已断开')
            status_led.setStyleSheet("color: red; font-size: 16px;")
            connect_button.setEnabled(True)  # 启用连接按钮
            disconnect_button.setEnabled(False)  # 禁用断开连接按钮
        except Exception as e:
            status_led.setText('连接状态: 断开失败')
            status_led.setStyleSheet("color: red; font-size: 16px;")
            print("断开失败:", e)

