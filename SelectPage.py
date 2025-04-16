from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QInputDialog
from demo import Ui_MainWindow


class SelectPage(QMainWindow, Ui_MainWindow):
    def __init__(self, pushButton_select, label_select):
        super().__init__()
        self.pushButton_select = pushButton_select
        self.label_select = label_select
        # 连接按钮的点击信号到槽函数
        self.pushButton_select.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        # 创建一个下拉框选择对话框
        items = ["探针1", "探针2"]  # 下拉框的选项

        # 创建 QInputDialog 对象
        dialog = QInputDialog(self)
        dialog.setWindowTitle("选择探针")
        dialog.setLabelText("请选择探针：")
        dialog.setComboBoxItems(items)
        dialog.setComboBoxEditable(False)
        # 更改窗口图标
        dialog.setWindowIcon(QIcon("kupai.png"))  # 替换为你的图标路径

        # 禁用问号按钮
        dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        # 显示对话框并获取用户的选择
        ok = dialog.exec_()
        selected_item = dialog.textValue()

        # 根据用户的选择进行处理
        if ok and selected_item:
            # 更新标签内容
            self.label_select.setText(f"当前选择：{selected_item}")
        else:
            # 如果用户取消选择，重置为无
            self.label_select.setText("当前选择：无")
