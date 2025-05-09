import sys

from MoveClass import MoveClass
from QTneedle.QTneedle.locationClass import locationClass
from StopClass import StopClass

# 定义你要添加的库文件路径
custom_lib_path = "c:\\users\\administrator\\appdata\\local\\programs\\python\\python37\\lib\\site-packages"

# 将路径添加到 sys.path
if custom_lib_path not in sys.path:
    sys.path.append(custom_lib_path)
import ctypes


from datetime import datetime

import cv2

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow



from CameraPage import CameraPage
from MainPage import MainPage1
from MicroPage import MicroPage
from NeedlePage import NeedlePage
from ScriptPage import ScriptPage
from SerialPage import SerialPage, NeedelConnectionThread
from SelectPage import SelectPage
from demo import Ui_MainWindow
from full_screen import show_custom_fullscreen

log_file = f"operation_log_{datetime.now().strftime('%Y-%m-%d')}.txt"


class UsingTest(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(UsingTest, self).__init__(*args, **kwargs)

        self.setupUi(self)  # 初始化ui
        show_custom_fullscreen(self)  # 自定义全屏模式，运行时直接进入全屏模式


        self.stopclass = StopClass(self.Button_needle1Stop)
        self.mainpage1 = MainPage1(self.label_video, self.label_cameraLabel, self.Button_screenshot, self.lineEdit_savePath, self.Button_browse, self.Button_needleTemplate,
                                   self.Button_padTemplate,self.Button_iuCalculate, self.plainTextEdit_log,log_file,self.Checkbox_microAutoTrace,self.Checkbox_ElecNeedle,self.Checkbox_Light,
                                   self.Button_Micro_up, self.Button_Micro_down, self.Button_Micro_left,self.Button_Micro_right,
                                   self.Button_needle1Up, self.Button_needle1Down, self.Button_needle1Left, self.Button_needle1Right,
                                   self.lineEdit_needle1Xdistance,self.lineEdit_needle1Ydistance, self.lineEdit_needle1Zdistance,
                                   self.Button_needle1SetXdisConfirm,self.Button_needle1SetYdisConfirm, self.Button_needle1SetZdisConfirm, self.label_light,
                                   self.lineEdit_SIM928, self.Button_SIM928,
                                   self.Button_pushing, self.Button_pulling, self.Button_relay,
                                   self.label_needle1,self.lineEdit_SaveResult)
        self.mainpage2 = SerialPage(self.comboBox_micro, self.label_microConnect, self.Button_microConnect,
                                    self.Button_microDisConnect,
                                    self.comboBox_needle, self.label_needleConnect, self.Button_needleConnect,
                                    self.Button_needleDisConnect,
                                    self.comboBox_SIM928_port1, self.comboBox_SIM928_port2, self.label_SIM928Connect,
                                    self.Button_SIM928Connect, self.Button_SIM928DisConnect,
                                    self.comboBox_SIM970_port1, self.comboBox_SIM970_port2, self.label_SIM970Connect,
                                    self.Button_SIM970Connect, self.Button_SIM970DisConnect,
                                    self.GBIO_connect_button,
                                    self.comboBox_relay, self.label_relayConnect, self.Button_relayConnect,
                                    self.Button_relayDisConnect,self.Serial_connect_refresh)

        self.mainpage3 = CameraPage(self.lineEdit_cameraBao, self.lineEdit_cameraGain, self.lineEdit_cameraRate, self.Button_cameraConfirm)
        self.mainpage4 = MicroPage(self.lineEdit_microSetXdis, self.lineEdit_microSetYdis, self.pushButton_MicroConfirm)
        self.mainpage5 = NeedlePage(self.lineEdit_needleSetXdis, self.lineEdit_needleSetYdis, self.lineEdit_needleSetZdis,
                                    self.lineEdit_needleSetXvol, self.lineEdit_needleSetYvol, self.lineEdit_needleSetZvol,
                                    self.lineEdit_needleSetXfreq, self.lineEdit_needleSetYfreq, self.lineEdit_needleSetZfreq, self.Button_needleSetConfirm)
        self.mainpage6 = ScriptPage(self.lineEdit_Scripts, self.Button_ScriptsBrowse, self.textEdit_Scripts, self.Button_scriptConfirm,
                                    self.lineEdit_SaveResult,self.Button_SaveResultBrowse,self.Button_scriptUpdate)
        self.mainpage7 = SelectPage(self.pushButton_select, self.label_select)
        self.locationClass = locationClass( self.lineEdit_Xlocation,self.lineEdit_Ylocation,self.lineEdit_Zlocation,
                                   self.lineEdit_Location1,self.lineEdit_Location2,self.lineEdit_Location3,
                                   self.Button_Location1,self.Button_Location2,self.Button_Location3,
                                   self.lineEdit_row,self.lineEdit_col,self.Button_CreateMap,self.mainpage1,
                                   self.Button_ContinueTest,self.Button_StopTest,
                                   self.lineEdit_Pushlocation,self.lineEdit_Pulllocation,
                                            self.Button_PushLocation,self.Button_PullLocation,
                                            self.Button_PushBack,self.Button_PullBack,self.lineEdit_Scripts,self.lineEdit_SaveResult)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建窗口程序
    app.setWindowIcon(QIcon('kupai.png'))  # 设置应用程序图标

    # 设置任务栏图标（Windows 特定）
    myappid = 'mycompany.myproduct.subproduct.version'  # 任意唯一字符串
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    win = UsingTest()
    win.show()
    sys.exit(app.exec())
