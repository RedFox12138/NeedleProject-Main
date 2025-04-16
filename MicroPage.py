from PyQt5.QtWidgets import QMainWindow, QMessageBox

from MainPage import MainPage1
from demo import Ui_MainWindow


class MicroPage(QMainWindow, Ui_MainWindow):
    def __init__(self,lineEdit_microSetXdis,lineEdit_microSetYdis,pushButton_MicroConfirm):
        super().__init__()
        self.lineEdit_microSetXdis = lineEdit_microSetXdis
        self.lineEdit_microSetYdis = lineEdit_microSetYdis
        self.lineEdit_microSetXdis.setText(str(MainPage1.micro_distanceX))
        self.lineEdit_microSetYdis.setText(str(MainPage1.micro_distanceY))
        pushButton_MicroConfirm.clicked.connect(self.update_micro_parameters)

    def update_micro_parameters(self):
        try:
            # 获取用户输入并转换为相应类型
            new_micro_Xmove = float(self.lineEdit_microSetXdis.text())
            new_micro_Ymove = float(self.lineEdit_microSetYdis.text())


            # 更新类属性
            MainPage1.micro_distanceX = new_micro_Xmove
            MainPage1.micro_distanceY = new_micro_Ymove


            # 显示成功消息
            QMessageBox.information(self, "成功", "显微镜参数已成功更新！")

            # 如果需要，可以在这里添加代码，将新参数应用到探针设备
            # 例如：self.apply_probe_settings()

        except (AttributeError,ValueError):
            # 如果输入无效，显示错误消息
            QMessageBox.warning(self, "输入错误", "请确保所有参数输入正确，或者检查探针是否连接")