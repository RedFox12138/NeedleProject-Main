import time

from PyQt5.QtWidgets import QMainWindow
import serial.tools.list_ports
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from pymeasure.instruments.keithley import Keithley2450

from SRS_SIM970 import SRSSIM970
from ZauxdllTest import GBIOConnect
from demo import Ui_MainWindow
import sys
# 定义你要添加的库文件路径
custom_lib_path = "c:\\users\\administrator\\appdata\\local\\programs\\python\\python37\\lib\\site-packages"

# 将路径添加到 sys.path
if custom_lib_path not in sys.path:
    sys.path.append(custom_lib_path)

class SerialPage(QMainWindow, Ui_MainWindow):
    def __init__(self,comboBox_micro,status_led_micro,connect_button_micro,disconnect_button_micro,
                 comboBox_needle,status_led_needle,connect_button_needle,disconnect_button_needle,
                 comboBox1_SIM928,comboBox2_SIM928,status_led_SIM928,connect_button_SIM928,disconnect_button_SIM928,
                 comboBox1_SIM970,comboBox2_SIM970,status_led_SIM970,connect_button_SIM970,disconnect_button_SIM970,
                 GBIO_connect_button,
                 comboBox_relay,status_led_relay,Button_relayConnect,Button_relayDisConnect,Serial_connect_refresh):
        super().__init__()
        self.port_combo = comboBox_micro
        self.connect_button = connect_button_micro
        self.status_led = status_led_micro
        self.disconnect_button = disconnect_button_micro

        self.needle_port_combo = comboBox_needle
        self.needle_connect_button = connect_button_needle
        self.needle_status_led = status_led_needle
        self.needle_disconnect_button = disconnect_button_needle

        self.SIM928_GBIO_combo = comboBox1_SIM928
        self.SIM928_port_combo = comboBox2_SIM928
        self.SIM928_connect_button = connect_button_SIM928
        self.SIM928_status_led = status_led_SIM928
        self.SIM928_disconnect_button = disconnect_button_SIM928

        self.SIM970_GBIO_combo = comboBox1_SIM970
        self.SIM970_port_combo = comboBox2_SIM970
        self.SIM970_connect_button = connect_button_SIM970
        self.SIM970_status_led = status_led_SIM970
        self.SIM970_disconnect_button = disconnect_button_SIM970


        self.comboBox_relay = comboBox_relay
        self.Button_relayConnect = Button_relayConnect
        self.Button_relayDisConnect = Button_relayDisConnect
        self.relay_status_led = status_led_relay

        self.update_serial_ports(self.comboBox_relay)  # 更新可用串口
        self.Button_relayConnect.clicked.connect(lambda: self.connect_to_serial('relay'))
        self.relay_status_led.setStyleSheet("color: red; font-size: 20px;")
        self.Button_relayDisConnect.setEnabled(False)  # 初始为禁用
        self.Button_relayDisConnect.clicked.connect(
        lambda: self.disconnect_from_serial("relay", self.relay_status_led, self.Button_relayConnect,
                                            self.Button_relayDisConnect))

        self.update_serial_ports(self.port_combo)  # 更新可用串口
        self.connect_button.clicked.connect(lambda: self.connect_to_serial('micro'))
        self.status_led.setStyleSheet("color: red; font-size: 20px;")
        self.disconnect_button.setEnabled(False)  # 初始为禁用
        self.disconnect_button.clicked.connect(
        lambda: self.disconnect_from_serial("micro", self.status_led, self.connect_button, self.disconnect_button))

        self.update_serial_ports(self.needle_port_combo)  # 更新可用串口
        self.needle_connect_button.clicked.connect(lambda: self.connect_to_serial('needle'))
        self.needle_status_led.setStyleSheet("color: red; font-size: 20px;")
        self.needle_disconnect_button.setEnabled(False)  # 初始为禁用
        self.needle_disconnect_button.clicked.connect(
            lambda: self.disconnect_from_serial("needle", self.needle_status_led,
                                                self.needle_connect_button, self.needle_disconnect_button))

        self.update_GBIO_ports(self.SIM928_GBIO_combo)  # 更新可用串口
        for num in range(1, 11):
            self.SIM928_port_combo.addItem(str(num))  # 添加串口设备名称
        self.SIM928_connect_button.clicked.connect(lambda: self.connect_to_serial('SIM928'))
        self.SIM928_status_led.setStyleSheet("color: red; font-size: 20px;")
        self.SIM928_disconnect_button.setEnabled(False)  # 初始为禁用
        self.SIM928_disconnect_button.clicked.connect(
            lambda: self.disconnect_from_serial("SIM928", self.SIM928_status_led,
                                                self.SIM928_connect_button, self.SIM928_disconnect_button))

        self.update_GBIO_ports(self.SIM970_GBIO_combo)  # 更新可用串口
        for num in range(1, 11):
            self.SIM970_port_combo.addItem(str(num))  # 添加串口设备名称
        self.SIM970_connect_button.clicked.connect(lambda: self.connect_to_serial('SIM970'))
        self.SIM970_status_led.setStyleSheet("color: red; font-size: 20px;")
        self.SIM970_disconnect_button.setEnabled(False)  # 初始为禁用
        self.SIM970_disconnect_button.clicked.connect(
            lambda: self.disconnect_from_serial("SIM970", self.SIM970_status_led,
                                                self.SIM970_connect_button, self.SIM970_disconnect_button))

        GBIO_connect_button.clicked.connect(
            self.GBIO_clicked
        )

        Serial_connect_refresh.clicked.connect(
            self.Serial_clicked
        )

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



    def Serial_clicked(self):
        self.update_serial_ports(self.needle_port_combo)
        self.update_serial_ports(self.comboBox_relay)
        self.update_serial_ports(self.port_combo)

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
            self.status_led.setStyleSheet("color: red; font-size: 20px;")
            return

        needle_selected_port = self.needle_port_combo.currentText()
        if not needle_selected_port:
            self.needle_status_led.setText('连接状态: 无串口可用')
            self.needle_status_led.setStyleSheet("color: red; font-size: 20px;")
            return

        SIM928_selected_GBIO = self.SIM928_GBIO_combo.currentText()
        SIM928_selected_port = self.SIM928_port_combo.currentText()
        if not SIM928_selected_GBIO or not SIM928_selected_port:
            self.SIM928_status_led.setText('连接状态: 无串口可用')
            self.SIM928_status_led.setStyleSheet("color: red; font-size: 20px;")
            return

        SIM970_selected_GBIO = self.SIM970_GBIO_combo.currentText()
        SIM970_selected_port = self.SIM970_port_combo.currentText()
        if not SIM970_selected_GBIO or not SIM970_selected_port:
            self.SIM970_status_led.setText('连接状态: 无串口可用')
            self.SIM970_status_led.setStyleSheet("color: red; font-size: 20px;")
            return

        relay_selected_port = self.comboBox_relay.currentText()
        if not relay_selected_port:
            self.relay_status_led.setText('连接状态: 无串口可用')
            self.relay_status_led.setStyleSheet("color: red; font-size: 20px;")
            return
        # 启动超时计时器
        self.timer.start()

        TEMP = selected_port[3:]
        # 启动连接线程
        port_number = int(selected_port[3:])  # 假设串口为 COMx 格式，取 x
        needle_prot_number = int(needle_selected_port[3:])
        relay_prot_number = int(relay_selected_port[3:])
        SIM928_GBIO_number = SIM928_selected_GBIO
        SIM928_prot_number = int(SIM928_selected_port[-1])
        SIM970_GBIO_number = SIM970_selected_GBIO
        SIM970_prot_number = int(SIM970_selected_port[-1])

        if(flag=="micro"):
            self.connection_thread = SerialConnectionThread(port_number)
            self.connection_thread.connected.connect(self.handle_connection_result)
            self.connection_thread.start()
            self.connect_button.setEnabled(False)
            self.disconnect_button.setEnabled(False)
        elif(flag=="needle"):
            self.connection_thread = NeedelConnectionThread(needle_prot_number)
            self.connection_thread.connected.connect(self.needle_handle_connection_result)
            self.connection_thread.start()
            self.needle_connect_button.setEnabled(False)
            self.needle_disconnect_button.setEnabled(False)
        elif (flag == "relay"):
            self.connection_thread = RelayConnectionThread(relay_prot_number)
            self.connection_thread.connected.connect(self.relay_handle_connection_result)
            self.connection_thread.start()
            self.Button_relayConnect.setEnabled(False)
            self.Button_relayDisConnect.setEnabled(False)
        elif(flag=="SIM928"):
            self.connection_thread = SIM928ConnectionThread(SIM928_prot_number,SIM928_GBIO_number)
            self.connection_thread.connected.connect(self.SIM928_handle_connection_result)
            self.connection_thread.start()
            self.SIM928_connect_button.setEnabled(False)
            self.SIM928_disconnect_button.setEnabled(False)
        elif(flag=="SIM970"):
            self.connection_thread = SIM970ConnectionThread(SIM970_prot_number, SIM970_GBIO_number)
            self.connection_thread.connected.connect(self.SIM970_handle_connection_result)
            self.connection_thread.start()
            self.SIM970_connect_button.setEnabled(False)
            self.SIM970_disconnect_button.setEnabled(False)


    def connection_timeout(self):
        """ 超时处理：2秒内没有连接成功，判定为连接失败 """
        if self.connection_thread and self.connection_thread.isRunning():
            self.status_led.setText('连接状态: 连接超时，请检查串口')
            self.status_led.setStyleSheet("color: red; font-size: 20px;")
            self.timer.stop()  # 停止计时器
            self.connect_button.setEnabled(True)  # 启用连接按钮
            self.disconnect_button.setEnabled(False)  # 禁用断开连接按钮

    def handle_connection_result(self, success, message):
        """ 处理连接成功或失败的信号 """
        if success:
            self.status_led.setText(f'连接状态: {message}')
            self.status_led.setStyleSheet("color: green; font-size: 20px;")
            self.connect_button.setEnabled(False)  # 禁用连接按钮
            self.disconnect_button.setEnabled(True)  # 启用断开连接按钮
        else:
            self.status_led.setText(f'连接状态: {message}')
            self.status_led.setStyleSheet("color: red; font-size: 20px;")
            self.connect_button.setEnabled(True)  # 启用连接按钮
            self.disconnect_button.setEnabled(False)  # 禁用断开连接按钮

        self.timer.stop()  # 停止计时器

    def needle_handle_connection_result(self, success, message):
        """ 处理连接成功或失败的信号 """
        if success:
            self.needle_status_led.setText(f'连接状态: {message}')
            self.needle_status_led.setStyleSheet("color: green; font-size: 20px;")
            self.needle_connect_button.setEnabled(False)  # 禁用连接按钮
            self.needle_disconnect_button.setEnabled(True)  # 启用断开连接按钮
        else:
            self.needle_status_led.setText(f'连接状态: {message}')
            self.needle_status_led.setStyleSheet("color: red; font-size: 20px;")
            self.needle_connect_button.setEnabled(True)  # 启用连接按钮
            self.needle_disconnect_button.setEnabled(False)  # 禁用断开连接按钮
        self.timer.stop()  # 停止计时器

    def relay_handle_connection_result(self, success, message):
        """ 处理连接成功或失败的信号 """
        if success:
            self.relay_status_led.setText(f'连接状态: {message}')
            self.relay_status_led.setStyleSheet("color: green; font-size: 20px;")
            self.Button_relayConnect.setEnabled(False)  # 禁用连接按钮
            self.Button_relayDisConnect.setEnabled(True)  # 启用断开连接按钮
        else:
            self.relay_status_led.setText(f'连接状态: {message}')
            self.relay_status_led.setStyleSheet("color: red; font-size: 20px;")
            self.Button_relayConnect.setEnabled(True)  # 启用连接按钮
            self.Button_relayDisConnect.setEnabled(False)  # 禁用断开连接按钮
        self.timer.stop()  # 停止计时器

    def SIM928_handle_connection_result(self, success, message):
        """ 处理连接成功或失败的信号 """
        if success:
            self.SIM928_status_led.setText(f'连接状态: {message}')
            self.SIM928_status_led.setStyleSheet("color: green; font-size: 20px;")
            self.SIM928_connect_button.setEnabled(False)  # 禁用连接按钮
            self.SIM928_disconnect_button.setEnabled(True)  # 启用断开连接按钮
        else:
            self.SIM928_status_led.setText(f'连接状态: {message}')
            self.SIM928_status_led.setStyleSheet("color: red; font-size: 20px;")
            self.SIM928_connect_button.setEnabled(True)  # 启用连接按钮
            self.SIM928_disconnect_button.setEnabled(False)  # 禁用断开连接按钮
        self.timer.stop()  # 停止计时器

    def SIM970_handle_connection_result(self, success, message):
        """ 处理连接成功或失败的信号 """
        if success:
            self.SIM970_status_led.setText(f'连接状态: {message}')
            self.SIM970_status_led.setStyleSheet("color: green; font-size: 20px;")
            self.SIM970_connect_button.setEnabled(False)  # 禁用连接按钮
            self.SIM970_disconnect_button.setEnabled(True)  # 启用断开连接按钮
        else:
            self.SIM970_status_led.setText(f'连接状态: {message}')
            self.SIM970_status_led.setStyleSheet("color: red; font-size: 20px;")
            self.SIM970_connect_button.setEnabled(True)  # 启用连接按钮
            self.SIM970_disconnect_button.setEnabled(False)  # 禁用断开连接按钮
        self.timer.stop()  # 停止计时器

    def disconnect_from_serial(self,flag,status_led,connect_button,disconnect_button):
        """ 断开串口连接 """
        try:
            if (flag == "micro"):
                if SerialConnectionThread.zaux:
                    SerialConnectionThread.zaux.disconnect()
            elif (flag == "needle"):
                NeedelConnectionThread.anc = None
            elif (flag == "relay"):
                RelayConnectionThread.anc = None
            elif (flag == "SIM928"):
                SIM928ConnectionThread.anc.shutdown()
                SIM928ConnectionThread.anc = None
            elif (flag == "SIM970"):
                SIM970ConnectionThread.anc.quit_vol()
                SIM970ConnectionThread.anc = None

            status_led.setText('连接状态: 已断开')
            status_led.setStyleSheet("color: red; font-size: 20px;")
            connect_button.setEnabled(True)  # 启用连接按钮
            disconnect_button.setEnabled(False)  # 禁用断开连接按钮
        except Exception as e:
            status_led.setText('连接状态: 断开失败')
            status_led.setStyleSheet("color: red; font-size: 20px;")
            print("断开失败:", e)

#位移器的串口连接
class SerialConnectionThread(QThread):
    # 定义信号，用来通知主界面连接成功或失败
    connected = pyqtSignal(bool, str)
    zaux = None
    port_com = 1

    def __init__(self, port_com):
        super().__init__()
        SerialConnectionThread.port_com = port_com

    def run(self):
        """ 运行连接操作 """
        try:
            self.connected.emit(True, f"连接成功，端口 {SerialConnectionThread.port_com}")
        except Exception as e:
            self.connected.emit(False, f"连接失败: {str(e)}")


class NeedelConnectionThread(QThread):
    # 定义信号，用来通知主界面连接成功或失败
    connected = pyqtSignal(bool, str)
    anc = None
    port_number = 1

    def __init__(self, port_number):
        super().__init__()
        NeedelConnectionThread.port_number = port_number

    def run(self):
        """ 运行连接操作 """
        try:
            bps = 115200  # 波特率（数据传输速率）
            port = "COM"+str(NeedelConnectionThread.port_number)  # 串口号（Windows系统常用COM格式）
            NeedelConnectionThread.anc = serial.Serial(port, bps, timeout=0.1)  # 创建串口对象，设置超时0.1秒
            self.connected.emit(True, f"连接成功，端口 {NeedelConnectionThread.port_number}")
        except Exception as e:
            self.connected.emit(False, f"连接失败: {str(e)}")

class RelayConnectionThread(QThread):
    # 定义信号，用来通知主界面连接成功或失败
    connected = pyqtSignal(bool, str)
    anc = None
    def __init__(self, port_number):
        super().__init__()
        self.port_number = port_number

    def run(self):
        """ 运行连接操作 """
        try:
            serialPort = self.port_number  # 串口
            baudRate = 9600  # 波特率
            RelayConnectionThread.anc = serial.Serial("COM"+str(serialPort), baudRate, timeout=0.5)

            print("参数设置：串口={0} ，波特率={1}".format(serialPort, baudRate))
            self.connected.emit(True, f"连接成功，端口 {self.port_number}")
        except Exception as e:
            self.connected.emit(False, f"连接失败: {str(e)}")


class SIM928ConnectionThread(QThread):
    # 定义信号，用来通知主界面连接成功或失败
    connected = pyqtSignal(bool, str)
    anc = None
    def __init__(self, port_number,GBIO_number):
        super().__init__()
        # self.port_number = port_number
        self.GBIO_number = GBIO_number
    def run(self):
        """ 运行连接操作 """
        try:
            SIM928ConnectionThread.anc = Keithley2450(self.GBIO_number)  # keithley2450地址
            keithley = SIM928ConnectionThread.anc
            keithley.reset()  # keithley2450初始化
            time.sleep(0.1)
            # 测量部分

            # SIM928ConnectionThread.anc = SIM928(self.port_number, self.GBIO_number)
            self.connected.emit(True, f"连接成功，端口 {self.GBIO_number}")
        except Exception as e:
            SIM928ConnectionThread.anc.shutdown()
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