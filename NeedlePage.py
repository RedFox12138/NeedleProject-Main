import time

from PyQt5.QtWidgets import QMainWindow, QMessageBox

from MainPage import MainPage1
from SerialPage import NeedelConnectionThread
from demo import Ui_MainWindow


class NeedlePage(QMainWindow, Ui_MainWindow):
    def __init__(self,lineEdit_needleSetXdis,lineEdit_needleSetYdis,lineEdit_needleSetZdis,
                                    lineEdit_needleSetXvol,lineEdit_needleSetYvol,lineEdit_needleSetZvol,
                                    lineEdit_needleSetXfreq,lineEdit_needleSetYfreq,lineEdit_needleSetZfreq,Button_needleSetConfirm):
        super().__init__()

        self.lineEdit_needleSetXdis = lineEdit_needleSetXdis
        self.lineEdit_needleSetYdis = lineEdit_needleSetYdis
        self.lineEdit_needleSetZdis = lineEdit_needleSetZdis
        self.lineEdit_needleSetXvol = lineEdit_needleSetXvol
        self.lineEdit_needleSetYvol = lineEdit_needleSetYvol
        self.lineEdit_needleSetZvol = lineEdit_needleSetZvol
        self.lineEdit_needleSetXfreq = lineEdit_needleSetXfreq
        self.lineEdit_needleSetYfreq = lineEdit_needleSetYfreq
        self.lineEdit_needleSetZfreq = lineEdit_needleSetZfreq
        self.Button_needleSetConfirm = Button_needleSetConfirm

        self.needle_voltageX = float(self.lineEdit_needleSetXvol.text())  # 探针X轴电压
        self.needle_voltageY = float(self.lineEdit_needleSetYvol.text())
        self.needle_voltageZ = float(self.lineEdit_needleSetZvol.text())
        self.needle_frequencyX = float(self.lineEdit_needleSetXfreq.text())  # 探针X轴频率
        self.needle_frequencyY = float(self.lineEdit_needleSetYfreq.text())
        self.needle_frequencyZ = float(self.lineEdit_needleSetZfreq.text())
        MainPage1.needle_distanceX = float(self.lineEdit_needleSetXdis.text())
        MainPage1.needle_distanceY = float(self.lineEdit_needleSetYdis.text())
        MainPage1.needle_distanceZ = float(self.lineEdit_needleSetZdis.text())


        Button_needleSetConfirm.clicked.connect(self.update_needle_parameters)


    def update_needle_parameters(self):
        try:
            # 获取用户输入并转换为相应类型
            new_needle_Xmove = float(self.lineEdit_needleSetXdis.text())
            new_needle_Ymove = float(self.lineEdit_needleSetYdis.text())
            new_needle_Zmove = float(self.lineEdit_needleSetZdis.text())
            new_VoltageX = float(self.lineEdit_needleSetXvol.text())
            new_FrequencyX = float(self.lineEdit_needleSetXfreq.text())
            new_VoltageY = float(self.lineEdit_needleSetYvol.text())
            new_FrequencyY = float(self.lineEdit_needleSetYfreq.text())
            new_VoltageZ = float(self.lineEdit_needleSetZvol.text())
            new_FrequencyZ = float(self.lineEdit_needleSetZfreq.text())

            # 更新类属性
            MainPage1.needle_distanceX = new_needle_Xmove
            MainPage1.needle_distanceY = new_needle_Ymove
            MainPage1.needle_distanceZ = new_needle_Zmove
            self.needle_voltageX = new_VoltageX
            self.needle_frequencyX = new_FrequencyX
            self.needle_voltageY = new_VoltageY
            self.needle_frequencyY = new_FrequencyY
            self.needle_voltageZ = new_VoltageZ
            self.needle_frequencyZ = new_FrequencyZ

            anc = NeedelConnectionThread.anc
            anc.write('[ch2:1]'.encode())
            anc.write('[cap:013nF]'.encode())
            anc.write(('[volt:+'+str(self.needle_voltageX)+'V] ').encode())
            anc.write(('[freq:+0'+str(self.needle_frequencyX)+'Hz]').encode())
            anc.write('[ch2:0]'.encode())
            time.sleep(0.2)
            anc.write('[ch3:1]'.encode())
            anc.write('[cap:013nF]'.encode())
            anc.write(('[volt:+' + str(self.needle_voltageY) + 'V] ').encode())
            anc.write(('[freq:+0' + str(self.needle_frequencyY) + 'Hz]').encode())
            anc.write('[ch3:0]'.encode())
            time.sleep(0.2)
            # 显示成功消息
            QMessageBox.information(self, "成功", "探针参数已成功更新！")

        except (AttributeError,ValueError):
            # 如果输入无效，显示错误消息
            QMessageBox.warning(self, "输入错误", "请确保所有参数输入正确，或者检查探针是否连接")
