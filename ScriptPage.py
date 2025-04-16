import os

from PyQt5.QtWidgets import QMainWindow, QFileDialog

from MainPage import MainPage1
from demo import Ui_MainWindow


class ScriptPage(QMainWindow, Ui_MainWindow):
    def __init__(self,lineEdit_Scripts,Button_ScriptsBrowse,textEdit_Scripts,Button_scriptConfirm,
                 lineEdit_SaveResult,Button_SaveResultBrowse):
        super().__init__()
        self.lineEdit_Scripts = lineEdit_Scripts
        self.lineEdit_SaveResult = lineEdit_SaveResult
        self.textEdit_Scripts = textEdit_Scripts

        self.textEdit_Scripts.setPlaceholderText("脚本内容将在此处显示...")
        self.textEdit_Scripts.setReadOnly(False)  # 设置为可读写

        Button_ScriptsBrowse.clicked.connect(self.browse_folder_script)
        Button_SaveResultBrowse.clicked.connect(self.browse_folder_Savescript)
        Button_scriptConfirm.clicked.disconnect() if Button_scriptConfirm.receivers(Button_scriptConfirm.clicked) > 0 else None
        Button_scriptConfirm.clicked.connect(self.save_script)


    def browse_folder_script(self):
        # 打开文件选择对话框，仅显示 .py 文件
        py_file, _ = QFileDialog.getOpenFileName(self, "选择一个 Python 文件", "", "Python Files (*.py)")
        if py_file:
            # 将选择的文件路径显示在文本框中
            self.lineEdit_Scripts.setText(py_file)

    def browse_folder_Savescript(self):
        # 打开文件选择对话框，仅显示 .py 文件
        folder_path = QFileDialog.getExistingDirectory(self, "选择一个文件夹", "")
        if folder_path:
            # 将选择的文件夹路径显示在文本框中
            self.lineEdit_SaveResult.setText(folder_path)
        MainPage1.save_script = self.lineEdit_SaveResult.text()

    def save_script(self):
        MainPage1.import_script = self.lineEdit_Scripts.text()
        file_path = MainPage1.import_script
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                self.textEdit_Scripts.setText(file.read())
        else:
            self.textEdit_Scripts.setText("文件路径无效，请检查路径。")