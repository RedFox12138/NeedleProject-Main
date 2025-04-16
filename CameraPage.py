from PyQt5.QtWidgets import QMainWindow, QMessageBox

from MainPage import MainPage1
from demo import Ui_MainWindow


class CameraPage(QMainWindow, Ui_MainWindow):
    def __init__(self,lineEdit_cameraBao,lineEdit_cameraGain,lineEdit_cameraRate,Button_cameraConfirm):
        super().__init__()
        # 初始相机参数
        self.baoGuang = 5000  # 初始曝光度
        self.gain = 6.03  # 初始增益
        self.rate = 59.8  # 初始帧率
        self.lineEdit_cameraBao = lineEdit_cameraBao
        self.lineEdit_cameraGain = lineEdit_cameraGain
        self.lineEdit_cameraRate = lineEdit_cameraRate
        self.lineEdit_cameraBao.setText(str(self.baoGuang))
        self.lineEdit_cameraGain.setText(str(self.gain))
        self.lineEdit_cameraRate.setText(str(self.rate))
        Button_cameraConfirm.clicked.connect(self.update_camera_parameters)

    def update_camera_parameters(self):
        try:
            # 获取用户输入并转换为相应类型
            new_baoGuang = int(self.lineEdit_cameraBao.text())
            new_gain = float(self.lineEdit_cameraGain.text())
            new_rate = float(self.lineEdit_cameraRate.text())

            # 更新类属性
            self.baoGuang = new_baoGuang
            self.gain = new_gain
            self.rate = new_rate
            MainPage1.obj_cam_operation.Set_parameter(self.rate, self.baoGuang, self.gain)

            # 显示成功消息
            QMessageBox.information(self, "成功", "相机参数已成功更新！")

            # 如果需要，可以在这里添加代码，将新参数应用到相机设备
            # 例如：self.apply_camera_settings()

        except ValueError:
            # 如果输入无效，显示错误消息
            QMessageBox.warning(self, "输入错误", "请确保所有参数输入正确。")