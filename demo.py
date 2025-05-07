# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2269, 1123)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(True)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: #c8c8c8; /* 深灰色背景 */\n"
"    font-family: \"Segoe UI\", sans-serif; \n"
"    font-size: 20px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 70, 2131, 931))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabBar::tab {\n"
"    width: 150px; /* 设置标签宽度 */\n"
"    height: 40px; /* 设置标签高度 */\n"
"    background-color: #d0d0d0; /* 标签默认背景颜色 */\n"
"    color: #000000; /* 标签默认文字颜色 */\n"
"    border: 1px solid #a0a0a0; /* 标签边框 */\n"
"    border-bottom-color: #b0b0b0; /* 底部边框颜色 */\n"
"    font-size: 30px; /* 字体大小 */\n"
"    padding: 5px; /* 内边距 */\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #b0b0b0; /* 选中标签的背景颜色 */\n"
"    color: #ffffff; /* 选中标签的文字颜色 */\n"
"    border-bottom-color: #b0b0b0; /* 选中标签的底部边框颜色 */\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background-color: #c0c0c0; /* 悬停标签的背景颜色 */\n"
"}\n"
"\n"
"QTabWidget {\n"
"    background-color: #b0b0b0; /* 标签页内容区域的背景颜色 */\n"
"    border: none; /* 去除默认边框 */\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #a0a0a0; /* 标签页内容区域的边框 */\n"
"    margin-top: -1px; /* 调整内容区域与标签栏的间距 */\n"
"}")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.plainTextEdit_log = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit_log.setGeometry(QtCore.QRect(1080, 700, 701, 161))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.plainTextEdit_log.setFont(font)
        self.plainTextEdit_log.setObjectName("plainTextEdit_log")
        self.label_video = QtWidgets.QLabel(self.tab)
        self.label_video.setEnabled(True)
        self.label_video.setGeometry(QtCore.QRect(10, 10, 1021, 851))
        self.label_video.setStyleSheet("#label_video{\n"
"border-width:2px;\n"
"border:2px solid;\n"
"border_color:rgb(255,255,127);\n"
"}")
        self.label_video.setText("")
        self.label_video.setObjectName("label_video")
        self.frame_6 = QtWidgets.QFrame(self.tab)
        self.frame_6.setGeometry(QtCore.QRect(1080, 80, 701, 281))
        self.frame_6.setStyleSheet("#frame_6{\n"
"border-width:2px;\n"
"border:2px solid;\n"
"border_color:rgb(255,255,127);\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame_6)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(70, 50, 221, 221))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Button_needle1Up = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_needle1Up.setFont(font)
        self.Button_needle1Up.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Vup.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_needle1Up.setIcon(icon)
        self.Button_needle1Up.setIconSize(QtCore.QSize(40, 40))
        self.Button_needle1Up.setFlat(True)
        self.Button_needle1Up.setObjectName("Button_needle1Up")
        self.gridLayout_2.addWidget(self.Button_needle1Up, 0, 1, 1, 1)
        self.Button_needle1Left = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_needle1Left.setFont(font)
        self.Button_needle1Left.setStyleSheet("QMainWindow {\n"
"    background-color: #808080;\n"
"}")
        self.Button_needle1Left.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Vleft.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_needle1Left.setIcon(icon1)
        self.Button_needle1Left.setIconSize(QtCore.QSize(40, 40))
        self.Button_needle1Left.setFlat(True)
        self.Button_needle1Left.setObjectName("Button_needle1Left")
        self.gridLayout_2.addWidget(self.Button_needle1Left, 1, 0, 1, 1)
        self.Button_needle1Down = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_needle1Down.setFont(font)
        self.Button_needle1Down.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Vdown.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_needle1Down.setIcon(icon2)
        self.Button_needle1Down.setIconSize(QtCore.QSize(40, 40))
        self.Button_needle1Down.setFlat(True)
        self.Button_needle1Down.setObjectName("Button_needle1Down")
        self.gridLayout_2.addWidget(self.Button_needle1Down, 2, 1, 1, 1)
        self.Button_needle1Right = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_needle1Right.setFont(font)
        self.Button_needle1Right.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Vright.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_needle1Right.setIcon(icon3)
        self.Button_needle1Right.setIconSize(QtCore.QSize(40, 40))
        self.Button_needle1Right.setFlat(True)
        self.Button_needle1Right.setObjectName("Button_needle1Right")
        self.gridLayout_2.addWidget(self.Button_needle1Right, 1, 2, 1, 1)
        self.Button_needle1Stop = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.Button_needle1Stop.setFont(font)
        self.Button_needle1Stop.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #ff4444, stop:1 #cc0000); /* 红色渐变背景 */\n"
"    border: 2px solid #cc0000; /* 边框颜色 */\n"
"    color: white; /* 文字颜色 */\n"
"    font-size: 30px; /* 字体大小 */\n"
"    font-weight: bold; /* 字体加粗 */\n"
"    text-align: center; /* 文字居中 */\n"
"    border-radius: 40px; /* 圆形按钮（半径设置为宽度和高度的一半） */\n"
"    min-width: 80px; /* 最小宽度 */\n"
"    min-height: 80px; /* 最小高度 */\n"
"    padding: 0; /* 去除内边距 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #0077ff, stop:1 #0044cc); /* 悬停时的蓝色渐变背景 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #cc0000, stop:1 #ff4444); /* 按下时的渐变背景 */\n"
"}")
        self.Button_needle1Stop.setObjectName("Button_needle1Stop")
        self.gridLayout_2.addWidget(self.Button_needle1Stop, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setGeometry(QtCore.QRect(340, 140, 38, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setGeometry(QtCore.QRect(340, 60, 39, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        self.label_2.setGeometry(QtCore.QRect(340, 100, 39, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_needle1Xdistance = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_needle1Xdistance.setGeometry(QtCore.QRect(390, 60, 61, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_needle1Xdistance.setFont(font)
        self.lineEdit_needle1Xdistance.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_needle1Xdistance.setObjectName("lineEdit_needle1Xdistance")
        self.lineEdit_needle1Ydistance = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_needle1Ydistance.setGeometry(QtCore.QRect(390, 100, 61, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_needle1Ydistance.setFont(font)
        self.lineEdit_needle1Ydistance.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_needle1Ydistance.setObjectName("lineEdit_needle1Ydistance")
        self.lineEdit_needle1Zdistance = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_needle1Zdistance.setGeometry(QtCore.QRect(390, 140, 61, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_needle1Zdistance.setFont(font)
        self.lineEdit_needle1Zdistance.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_needle1Zdistance.setObjectName("lineEdit_needle1Zdistance")
        self.Button_needle1SetXdisConfirm = QtWidgets.QPushButton(self.frame_6)
        self.Button_needle1SetXdisConfirm.setGeometry(QtCore.QRect(530, 50, 75, 32))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_needle1SetXdisConfirm.setFont(font)
        self.Button_needle1SetXdisConfirm.setObjectName("Button_needle1SetXdisConfirm")
        self.Button_needle1SetYdisConfirm = QtWidgets.QPushButton(self.frame_6)
        self.Button_needle1SetYdisConfirm.setGeometry(QtCore.QRect(460, 100, 75, 32))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_needle1SetYdisConfirm.setFont(font)
        self.Button_needle1SetYdisConfirm.setObjectName("Button_needle1SetYdisConfirm")
        self.Button_needle1SetZdisConfirm = QtWidgets.QPushButton(self.frame_6)
        self.Button_needle1SetZdisConfirm.setGeometry(QtCore.QRect(460, 140, 75, 32))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_needle1SetZdisConfirm.setFont(font)
        self.Button_needle1SetZdisConfirm.setObjectName("Button_needle1SetZdisConfirm")
        self.Button_pulling = QtWidgets.QPushButton(self.frame_6)
        self.Button_pulling.setGeometry(QtCore.QRect(340, 180, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_pulling.setFont(font)
        self.Button_pulling.setObjectName("Button_pulling")
        self.Button_pushing = QtWidgets.QPushButton(self.frame_6)
        self.Button_pushing.setGeometry(QtCore.QRect(460, 180, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_pushing.setFont(font)
        self.Button_pushing.setObjectName("Button_pushing")
        self.label_needle1 = QtWidgets.QLabel(self.frame_6)
        self.label_needle1.setGeometry(QtCore.QRect(10, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_needle1.setFont(font)
        self.label_needle1.setObjectName("label_needle1")
        self.label_needle1_2 = QtWidgets.QLabel(self.frame_6)
        self.label_needle1_2.setGeometry(QtCore.QRect(340, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_needle1_2.setFont(font)
        self.label_needle1_2.setObjectName("label_needle1_2")
        self.frame_7 = QtWidgets.QFrame(self.tab)
        self.frame_7.setGeometry(QtCore.QRect(1080, 370, 331, 321))
        self.frame_7.setStyleSheet("#frame_7{\n"
"border-width:2px;\n"
"border:2px solid;\n"
"border_color:rgb(255,255,127);\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label = QtWidgets.QLabel(self.frame_7)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_7)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 40, 221, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Button_Micro_right = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_Micro_right.setText("")
        self.Button_Micro_right.setIcon(icon3)
        self.Button_Micro_right.setIconSize(QtCore.QSize(40, 40))
        self.Button_Micro_right.setFlat(True)
        self.Button_Micro_right.setObjectName("Button_Micro_right")
        self.gridLayout.addWidget(self.Button_Micro_right, 1, 3, 1, 1)
        self.Button_Micro_down = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_Micro_down.setText("")
        self.Button_Micro_down.setIcon(icon2)
        self.Button_Micro_down.setIconSize(QtCore.QSize(40, 40))
        self.Button_Micro_down.setDefault(False)
        self.Button_Micro_down.setFlat(True)
        self.Button_Micro_down.setObjectName("Button_Micro_down")
        self.gridLayout.addWidget(self.Button_Micro_down, 2, 2, 1, 1)
        self.Button_Micro_up = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_Micro_up.setText("")
        self.Button_Micro_up.setIcon(icon)
        self.Button_Micro_up.setIconSize(QtCore.QSize(40, 40))
        self.Button_Micro_up.setFlat(True)
        self.Button_Micro_up.setObjectName("Button_Micro_up")
        self.gridLayout.addWidget(self.Button_Micro_up, 0, 2, 1, 1)
        self.Button_Micro_left = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_Micro_left.setText("")
        self.Button_Micro_left.setIcon(icon1)
        self.Button_Micro_left.setIconSize(QtCore.QSize(40, 40))
        self.Button_Micro_left.setFlat(True)
        self.Button_Micro_left.setObjectName("Button_Micro_left")
        self.gridLayout.addWidget(self.Button_Micro_left, 1, 0, 1, 1)
        self.frame_9 = QtWidgets.QFrame(self.tab)
        self.frame_9.setGeometry(QtCore.QRect(1450, 370, 331, 321))
        self.frame_9.setStyleSheet("#frame_9{\n"
"border-width:2px;\n"
"border:2px solid;\n"
"border_color:rgb(255,255,127);\n"
"}")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_6 = QtWidgets.QLabel(self.frame_9)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(self.frame_9)
        self.label_10.setGeometry(QtCore.QRect(10, 90, 81, 33))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.Button_SIM928 = QtWidgets.QPushButton(self.frame_9)
        self.Button_SIM928.setGeometry(QtCore.QRect(210, 60, 75, 32))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_SIM928.setFont(font)
        self.Button_SIM928.setObjectName("Button_SIM928")
        self.lineEdit_SIM970 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_SIM970.setGeometry(QtCore.QRect(100, 100, 101, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_SIM970.setFont(font)
        self.lineEdit_SIM970.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_SIM970.setPlaceholderText("")
        self.lineEdit_SIM970.setObjectName("lineEdit_SIM970")
        self.lineEdit_SIM928 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_SIM928.setGeometry(QtCore.QRect(100, 60, 101, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_SIM928.setFont(font)
        self.lineEdit_SIM928.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_SIM928.setObjectName("lineEdit_SIM928")
        self.label_9 = QtWidgets.QLabel(self.frame_9)
        self.label_9.setGeometry(QtCore.QRect(10, 50, 81, 33))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.Button_SIM970 = QtWidgets.QPushButton(self.frame_9)
        self.Button_SIM970.setGeometry(QtCore.QRect(210, 100, 75, 32))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_SIM970.setFont(font)
        self.Button_SIM970.setObjectName("Button_SIM970")
        self.label_25 = QtWidgets.QLabel(self.frame_9)
        self.label_25.setGeometry(QtCore.QRect(10, 140, 81, 33))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.frame_9)
        self.label_26.setGeometry(QtCore.QRect(10, 170, 81, 33))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_32 = QtWidgets.QLabel(self.frame_9)
        self.label_32.setGeometry(QtCore.QRect(10, 200, 81, 33))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.lineEdit_Location1 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_Location1.setGeometry(QtCore.QRect(60, 140, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_Location1.setFont(font)
        self.lineEdit_Location1.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_Location1.setObjectName("lineEdit_Location1")
        self.lineEdit_Location2 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_Location2.setGeometry(QtCore.QRect(60, 170, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_Location2.setFont(font)
        self.lineEdit_Location2.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_Location2.setObjectName("lineEdit_Location2")
        self.lineEdit_Location3 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_Location3.setGeometry(QtCore.QRect(60, 200, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_Location3.setFont(font)
        self.lineEdit_Location3.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_Location3.setObjectName("lineEdit_Location3")
        self.Button_Location1 = QtWidgets.QPushButton(self.frame_9)
        self.Button_Location1.setGeometry(QtCore.QRect(240, 140, 75, 32))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_Location1.setFont(font)
        self.Button_Location1.setObjectName("Button_Location1")
        self.Button_Location2 = QtWidgets.QPushButton(self.frame_9)
        self.Button_Location2.setGeometry(QtCore.QRect(240, 170, 75, 32))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_Location2.setFont(font)
        self.Button_Location2.setObjectName("Button_Location2")
        self.Button_Location3 = QtWidgets.QPushButton(self.frame_9)
        self.Button_Location3.setGeometry(QtCore.QRect(240, 200, 75, 32))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_Location3.setFont(font)
        self.Button_Location3.setObjectName("Button_Location3")
        self.lineEdit_row = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_row.setGeometry(QtCore.QRect(60, 240, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_row.setFont(font)
        self.lineEdit_row.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_row.setObjectName("lineEdit_row")
        self.lineEdit_col = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_col.setGeometry(QtCore.QRect(150, 240, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_col.setFont(font)
        self.lineEdit_col.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_col.setObjectName("lineEdit_col")
        self.label_35 = QtWidgets.QLabel(self.frame_9)
        self.label_35.setGeometry(QtCore.QRect(20, 240, 31, 33))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.label_37 = QtWidgets.QLabel(self.frame_9)
        self.label_37.setGeometry(QtCore.QRect(120, 240, 31, 33))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.Button_CreateMap = QtWidgets.QPushButton(self.frame_9)
        self.Button_CreateMap.setGeometry(QtCore.QRect(70, 280, 101, 32))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_CreateMap.setFont(font)
        self.Button_CreateMap.setObjectName("Button_CreateMap")
        self.Button_ContinueTest = QtWidgets.QPushButton(self.frame_9)
        self.Button_ContinueTest.setGeometry(QtCore.QRect(190, 280, 101, 32))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_ContinueTest.setFont(font)
        self.Button_ContinueTest.setObjectName("Button_ContinueTest")
        self.Button_StopTest = QtWidgets.QPushButton(self.frame_9)
        self.Button_StopTest.setGeometry(QtCore.QRect(200, 240, 101, 32))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_StopTest.setFont(font)
        self.Button_StopTest.setObjectName("Button_StopTest")
        self.Button_relay = QtWidgets.QPushButton(self.tab)
        self.Button_relay.setGeometry(QtCore.QRect(1080, 30, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_relay.setFont(font)
        self.Button_relay.setObjectName("Button_relay")
        self.Checkbox_ElecNeedle = QtWidgets.QRadioButton(self.tab)
        self.Checkbox_ElecNeedle.setGeometry(QtCore.QRect(1260, 30, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Checkbox_ElecNeedle.setFont(font)
        self.Checkbox_ElecNeedle.setChecked(True)
        self.Checkbox_ElecNeedle.setObjectName("Checkbox_ElecNeedle")
        self.Checkbox_Light = QtWidgets.QRadioButton(self.tab)
        self.Checkbox_Light.setGeometry(QtCore.QRect(1340, 30, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Checkbox_Light.setFont(font)
        self.Checkbox_Light.setObjectName("Checkbox_Light")
        self.lineEdit_Xlocation = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Xlocation.setGeometry(QtCore.QRect(1910, 30, 161, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_Xlocation.setFont(font)
        self.lineEdit_Xlocation.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_Xlocation.setObjectName("lineEdit_Xlocation")
        self.label_23 = QtWidgets.QLabel(self.tab)
        self.label_23.setGeometry(QtCore.QRect(1830, 30, 81, 33))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.lineEdit_Ylocation = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Ylocation.setGeometry(QtCore.QRect(1910, 70, 161, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_Ylocation.setFont(font)
        self.lineEdit_Ylocation.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_Ylocation.setObjectName("lineEdit_Ylocation")
        self.label_24 = QtWidgets.QLabel(self.tab)
        self.label_24.setGeometry(QtCore.QRect(1830, 70, 81, 33))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_38 = QtWidgets.QLabel(self.tab)
        self.label_38.setGeometry(QtCore.QRect(1830, 110, 81, 33))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.lineEdit_Zlocation = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Zlocation.setGeometry(QtCore.QRect(1910, 120, 161, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_Zlocation.setFont(font)
        self.lineEdit_Zlocation.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_Zlocation.setObjectName("lineEdit_Zlocation")
        self.lineEdit_Pushlocation = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Pushlocation.setGeometry(QtCore.QRect(1870, 170, 161, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_Pushlocation.setFont(font)
        self.lineEdit_Pushlocation.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_Pushlocation.setObjectName("lineEdit_Pushlocation")
        self.lineEdit_Pulllocation = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Pulllocation.setGeometry(QtCore.QRect(1870, 220, 161, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_Pulllocation.setFont(font)
        self.lineEdit_Pulllocation.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_Pulllocation.setObjectName("lineEdit_Pulllocation")
        self.label_39 = QtWidgets.QLabel(self.tab)
        self.label_39.setGeometry(QtCore.QRect(1810, 170, 81, 33))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.label_41 = QtWidgets.QLabel(self.tab)
        self.label_41.setGeometry(QtCore.QRect(1810, 220, 81, 33))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.Button_PushLocation = QtWidgets.QPushButton(self.tab)
        self.Button_PushLocation.setGeometry(QtCore.QRect(2040, 170, 75, 32))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_PushLocation.setFont(font)
        self.Button_PushLocation.setObjectName("Button_PushLocation")
        self.Button_PullLocation = QtWidgets.QPushButton(self.tab)
        self.Button_PullLocation.setGeometry(QtCore.QRect(2040, 220, 75, 32))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_PullLocation.setFont(font)
        self.Button_PullLocation.setObjectName("Button_PullLocation")
        self.Button_PushBack = QtWidgets.QPushButton(self.tab)
        self.Button_PushBack.setGeometry(QtCore.QRect(1810, 270, 111, 32))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_PushBack.setFont(font)
        self.Button_PushBack.setObjectName("Button_PushBack")
        self.Button_PullBack = QtWidgets.QPushButton(self.tab)
        self.Button_PullBack.setGeometry(QtCore.QRect(1930, 270, 111, 32))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_PullBack.setFont(font)
        self.Button_PullBack.setObjectName("Button_PullBack")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(460, 100, 321, 621))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 4, 0, 1, 1)
        self.Button_cameraConfirm = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_cameraConfirm.sizePolicy().hasHeightForWidth())
        self.Button_cameraConfirm.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_cameraConfirm.setFont(font)
        self.Button_cameraConfirm.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Button_cameraConfirm.setObjectName("Button_cameraConfirm")
        self.gridLayout_5.addWidget(self.Button_cameraConfirm, 8, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.lineEdit_cameraBao = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_cameraBao.setFont(font)
        self.lineEdit_cameraBao.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_cameraBao.setObjectName("lineEdit_cameraBao")
        self.gridLayout_5.addWidget(self.lineEdit_cameraBao, 3, 0, 1, 1)
        self.lineEdit_cameraRate = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_cameraRate.setFont(font)
        self.lineEdit_cameraRate.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_cameraRate.setObjectName("lineEdit_cameraRate")
        self.gridLayout_5.addWidget(self.lineEdit_cameraRate, 7, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 6, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 2, 0, 1, 1)
        self.lineEdit_cameraGain = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_cameraGain.setFont(font)
        self.lineEdit_cameraGain.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_cameraGain.setObjectName("lineEdit_cameraGain")
        self.gridLayout_5.addWidget(self.lineEdit_cameraGain, 5, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.gridLayoutWidget_5)
        self.frame_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_5.addWidget(self.frame_4, 1, 0, 1, 1)
        self.label_cameraLabel = QtWidgets.QLabel(self.tab_2)
        self.label_cameraLabel.setGeometry(QtCore.QRect(810, 200, 400, 400))
        self.label_cameraLabel.setStyleSheet("#label_cameraLabel{\n"
"border-width:2px;\n"
"border:0.5px solid;\n"
"border_color:rgb(255,255,127);\n"
"}")
        self.label_cameraLabel.setLineWidth(1)
        self.label_cameraLabel.setText("")
        self.label_cameraLabel.setObjectName("label_cameraLabel")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(1020, 0, 321, 621))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_5 = QtWidgets.QFrame(self.gridLayoutWidget_6)
        self.frame_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_6.addWidget(self.frame_5, 0, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(330, 170, 319, 125))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab_3)
        self.label_18.setGeometry(QtCore.QRect(330, 370, 255, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.lineEdit_microSetXdis = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_microSetXdis.setGeometry(QtCore.QRect(580, 220, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_microSetXdis.setFont(font)
        self.lineEdit_microSetXdis.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_microSetXdis.setObjectName("lineEdit_microSetXdis")
        self.lineEdit_microSetYdis = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_microSetYdis.setGeometry(QtCore.QRect(580, 370, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_microSetYdis.setFont(font)
        self.lineEdit_microSetYdis.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_microSetYdis.setObjectName("lineEdit_microSetYdis")
        self.pushButton_MicroConfirm = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_MicroConfirm.setGeometry(QtCore.QRect(730, 490, 75, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_MicroConfirm.sizePolicy().hasHeightForWidth())
        self.pushButton_MicroConfirm.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.pushButton_MicroConfirm.setFont(font)
        self.pushButton_MicroConfirm.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_MicroConfirm.setObjectName("pushButton_MicroConfirm")
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(320, 90, 140, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.Button_needleSetConfirm = QtWidgets.QPushButton(self.tab_4)
        self.Button_needleSetConfirm.setGeometry(QtCore.QRect(820, 650, 121, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_needleSetConfirm.sizePolicy().hasHeightForWidth())
        self.Button_needleSetConfirm.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_needleSetConfirm.setFont(font)
        self.Button_needleSetConfirm.setObjectName("Button_needleSetConfirm")
        self.layoutWidget = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 160, 1557, 421))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_30 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.gridLayout_7.addWidget(self.label_30, 2, 6, 1, 1)
        self.lineEdit_needleSetZfreq = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_needleSetZfreq.setFont(font)
        self.lineEdit_needleSetZfreq.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_needleSetZfreq.setObjectName("lineEdit_needleSetZfreq")
        self.gridLayout_7.addWidget(self.lineEdit_needleSetZfreq, 2, 7, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout_7.addWidget(self.label_20, 2, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.gridLayout_7.addWidget(self.label_28, 0, 6, 1, 1)
        self.lineEdit_needleSetZdis = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_needleSetZdis.setFont(font)
        self.lineEdit_needleSetZdis.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_needleSetZdis.setObjectName("lineEdit_needleSetZdis")
        self.gridLayout_7.addWidget(self.lineEdit_needleSetZdis, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 0, 2, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_7.addWidget(self.label_22, 1, 3, 1, 1)
        self.lineEdit_needleSetYdis = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_needleSetYdis.setFont(font)
        self.lineEdit_needleSetYdis.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_needleSetYdis.setObjectName("lineEdit_needleSetYdis")
        self.gridLayout_7.addWidget(self.lineEdit_needleSetYdis, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout_7.addWidget(self.label_19, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_27 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout_7.addWidget(self.label_27, 2, 3, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.gridLayout_7.addWidget(self.label_29, 1, 6, 1, 1)
        self.lineEdit_needleSetXvol = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_needleSetXvol.sizePolicy().hasHeightForWidth())
        self.lineEdit_needleSetXvol.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_needleSetXvol.setFont(font)
        self.lineEdit_needleSetXvol.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_needleSetXvol.setObjectName("lineEdit_needleSetXvol")
        self.gridLayout_7.addWidget(self.lineEdit_needleSetXvol, 0, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.lineEdit_needleSetXfreq = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_needleSetXfreq.sizePolicy().hasHeightForWidth())
        self.lineEdit_needleSetXfreq.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_needleSetXfreq.setFont(font)
        self.lineEdit_needleSetXfreq.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_needleSetXfreq.setObjectName("lineEdit_needleSetXfreq")
        self.gridLayout_7.addWidget(self.lineEdit_needleSetXfreq, 0, 7, 1, 1, QtCore.Qt.AlignHCenter)
        self.lineEdit_needleSetYfreq = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_needleSetYfreq.setFont(font)
        self.lineEdit_needleSetYfreq.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_needleSetYfreq.setObjectName("lineEdit_needleSetYfreq")
        self.gridLayout_7.addWidget(self.lineEdit_needleSetYfreq, 1, 7, 1, 1, QtCore.Qt.AlignHCenter)
        self.lineEdit_needleSetXdis = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_needleSetXdis.sizePolicy().hasHeightForWidth())
        self.lineEdit_needleSetXdis.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_needleSetXdis.setFont(font)
        self.lineEdit_needleSetXdis.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_needleSetXdis.setObjectName("lineEdit_needleSetXdis")
        self.gridLayout_7.addWidget(self.lineEdit_needleSetXdis, 0, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_7.addWidget(self.label_16, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_7.addWidget(self.label_21, 0, 3, 1, 1)
        self.lineEdit_needleSetZvol = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_needleSetZvol.setFont(font)
        self.lineEdit_needleSetZvol.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_needleSetZvol.setObjectName("lineEdit_needleSetZvol")
        self.gridLayout_7.addWidget(self.lineEdit_needleSetZvol, 2, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.lineEdit_needleSetYvol = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_needleSetYvol.setFont(font)
        self.lineEdit_needleSetYvol.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #a0a0a0;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #000000;\n"
"    selection-background-color: #c0c0c0;\n"
"    selection-color: #000000;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #606060;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #808080;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #d0d0d0;\n"
"    color: #808080;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.lineEdit_needleSetYvol.setObjectName("lineEdit_needleSetYvol")
        self.gridLayout_7.addWidget(self.lineEdit_needleSetYvol, 1, 4, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 0, 5, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayoutWidget_8 = QtWidgets.QWidget(self.tab_5)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(320, 50, 1161, 662))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.gridLayoutWidget_8.setFont(font)
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.Button_relayConnect = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_relayConnect.setFont(font)
        self.Button_relayConnect.setObjectName("Button_relayConnect")
        self.gridLayout_9.addWidget(self.Button_relayConnect, 16, 0, 1, 1)
        self.comboBox_relay = QtWidgets.QComboBox(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.comboBox_relay.setFont(font)
        self.comboBox_relay.setObjectName("comboBox_relay")
        self.gridLayout_9.addWidget(self.comboBox_relay, 15, 0, 1, 1)
        self.label_microConnect = QtWidgets.QLabel(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_microConnect.setFont(font)
        self.label_microConnect.setObjectName("label_microConnect")
        self.gridLayout_9.addWidget(self.label_microConnect, 5, 0, 1, 1)
        self.comboBox_micro = QtWidgets.QComboBox(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.comboBox_micro.setFont(font)
        self.comboBox_micro.setObjectName("comboBox_micro")
        self.gridLayout_9.addWidget(self.comboBox_micro, 1, 0, 1, 1)
        self.Button_SIM928Connect = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_SIM928Connect.setFont(font)
        self.Button_SIM928Connect.setObjectName("Button_SIM928Connect")
        self.gridLayout_9.addWidget(self.Button_SIM928Connect, 3, 2, 1, 1)
        self.Button_needleDisConnect = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_needleDisConnect.setFont(font)
        self.Button_needleDisConnect.setObjectName("Button_needleDisConnect")
        self.gridLayout_9.addWidget(self.Button_needleDisConnect, 11, 0, 1, 1)
        self.frame_12 = QtWidgets.QFrame(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.frame_12.setFont(font)
        self.frame_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_9.addWidget(self.frame_12, 13, 2, 1, 1)
        self.label_SIM928Connect = QtWidgets.QLabel(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_SIM928Connect.setFont(font)
        self.label_SIM928Connect.setObjectName("label_SIM928Connect")
        self.gridLayout_9.addWidget(self.label_SIM928Connect, 5, 2, 1, 1)
        self.label_relayConnect = QtWidgets.QLabel(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_relayConnect.setFont(font)
        self.label_relayConnect.setObjectName("label_relayConnect")
        self.gridLayout_9.addWidget(self.label_relayConnect, 18, 0, 1, 1)
        self.Button_SIM928DisConnect = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_SIM928DisConnect.setFont(font)
        self.Button_SIM928DisConnect.setObjectName("Button_SIM928DisConnect")
        self.gridLayout_9.addWidget(self.Button_SIM928DisConnect, 4, 2, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.gridLayout_9.addWidget(self.label_36, 7, 2, 1, 1)
        self.comboBox_SIM970_port2 = QtWidgets.QComboBox(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.comboBox_SIM970_port2.setFont(font)
        self.comboBox_SIM970_port2.setObjectName("comboBox_SIM970_port2")
        self.gridLayout_9.addWidget(self.comboBox_SIM970_port2, 9, 2, 1, 1)
        self.label_SIM970Connect = QtWidgets.QLabel(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_SIM970Connect.setFont(font)
        self.label_SIM970Connect.setObjectName("label_SIM970Connect")
        self.gridLayout_9.addWidget(self.label_SIM970Connect, 12, 2, 1, 1)
        self.frame_13 = QtWidgets.QFrame(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.frame_13.setFont(font)
        self.frame_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_9.addWidget(self.frame_13, 13, 0, 1, 1)
        self.label_62 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_62.setFont(font)
        self.label_62.setObjectName("label_62")
        self.gridLayout_9.addWidget(self.label_62, 14, 0, 1, 1)
        self.label_needleConnect = QtWidgets.QLabel(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_needleConnect.setFont(font)
        self.label_needleConnect.setObjectName("label_needleConnect")
        self.gridLayout_9.addWidget(self.label_needleConnect, 12, 0, 1, 1)
        self.Button_needleConnect = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_needleConnect.setFont(font)
        self.Button_needleConnect.setObjectName("Button_needleConnect")
        self.gridLayout_9.addWidget(self.Button_needleConnect, 10, 0, 1, 1)
        self.comboBox_SIM928_port2 = QtWidgets.QComboBox(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.comboBox_SIM928_port2.setFont(font)
        self.comboBox_SIM928_port2.setObjectName("comboBox_SIM928_port2")
        self.gridLayout_9.addWidget(self.comboBox_SIM928_port2, 2, 2, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.gridLayout_9.addWidget(self.label_31, 0, 0, 1, 1)
        self.comboBox_SIM970_port1 = QtWidgets.QComboBox(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.comboBox_SIM970_port1.setFont(font)
        self.comboBox_SIM970_port1.setObjectName("comboBox_SIM970_port1")
        self.gridLayout_9.addWidget(self.comboBox_SIM970_port1, 8, 2, 1, 1)
        self.Button_relayDisConnect = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_relayDisConnect.setFont(font)
        self.Button_relayDisConnect.setObjectName("Button_relayDisConnect")
        self.gridLayout_9.addWidget(self.Button_relayDisConnect, 17, 0, 1, 1)
        self.Button_SIM970Connect = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_SIM970Connect.setFont(font)
        self.Button_SIM970Connect.setObjectName("Button_SIM970Connect")
        self.gridLayout_9.addWidget(self.Button_SIM970Connect, 10, 2, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.gridLayout_9.addWidget(self.label_34, 0, 2, 1, 1)
        self.Button_microDisConnect = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_microDisConnect.setFont(font)
        self.Button_microDisConnect.setObjectName("Button_microDisConnect")
        self.gridLayout_9.addWidget(self.Button_microDisConnect, 4, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.gridLayout_9.addWidget(self.label_33, 7, 0, 1, 1)
        self.comboBox_SIM928_port1 = QtWidgets.QComboBox(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.comboBox_SIM928_port1.setFont(font)
        self.comboBox_SIM928_port1.setObjectName("comboBox_SIM928_port1")
        self.gridLayout_9.addWidget(self.comboBox_SIM928_port1, 1, 2, 1, 1)
        self.frame = QtWidgets.QFrame(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_9.addWidget(self.frame, 6, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_9.addWidget(self.frame_2, 6, 2, 1, 1)
        self.Button_SIM970DisConnect = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_SIM970DisConnect.setFont(font)
        self.Button_SIM970DisConnect.setObjectName("Button_SIM970DisConnect")
        self.gridLayout_9.addWidget(self.Button_SIM970DisConnect, 11, 2, 1, 1)
        self.Button_microConnect = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_microConnect.setFont(font)
        self.Button_microConnect.setObjectName("Button_microConnect")
        self.gridLayout_9.addWidget(self.Button_microConnect, 3, 0, 1, 1)
        self.comboBox_needle = QtWidgets.QComboBox(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.comboBox_needle.setFont(font)
        self.comboBox_needle.setObjectName("comboBox_needle")
        self.gridLayout_9.addWidget(self.comboBox_needle, 8, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_9.addWidget(self.frame_3, 0, 1, 19, 1)
        self.GBIO_connect_button = QtWidgets.QPushButton(self.tab_5)
        self.GBIO_connect_button.setGeometry(QtCore.QRect(1060, 720, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.GBIO_connect_button.setFont(font)
        self.GBIO_connect_button.setObjectName("GBIO_connect_button")
        self.Serial_connect_refresh = QtWidgets.QPushButton(self.tab_5)
        self.Serial_connect_refresh.setGeometry(QtCore.QRect(500, 720, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Serial_connect_refresh.setFont(font)
        self.Serial_connect_refresh.setObjectName("Serial_connect_refresh")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_6)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(380, 60, 1041, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.horizontalLayoutWidget.setFont(font)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_40 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.horizontalLayout.addWidget(self.label_40)
        self.lineEdit_Scripts = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_Scripts.setFont(font)
        self.lineEdit_Scripts.setObjectName("lineEdit_Scripts")
        self.horizontalLayout.addWidget(self.lineEdit_Scripts)
        self.Button_ScriptsBrowse = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_ScriptsBrowse.setFont(font)
        self.Button_ScriptsBrowse.setObjectName("Button_ScriptsBrowse")
        self.horizontalLayout.addWidget(self.Button_ScriptsBrowse)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_6)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(380, 230, 1041, 491))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.horizontalLayoutWidget_2.setFont(font)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit_Scripts = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.textEdit_Scripts.setFont(font)
        self.textEdit_Scripts.setObjectName("textEdit_Scripts")
        self.horizontalLayout_2.addWidget(self.textEdit_Scripts)
        self.Button_scriptConfirm = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_scriptConfirm.setFont(font)
        self.Button_scriptConfirm.setObjectName("Button_scriptConfirm")
        self.horizontalLayout_2.addWidget(self.Button_scriptConfirm)
        self.Button_scriptUpdate = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_scriptUpdate.setFont(font)
        self.Button_scriptUpdate.setObjectName("Button_scriptUpdate")
        self.horizontalLayout_2.addWidget(self.Button_scriptUpdate)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_6)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(380, 150, 1041, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.horizontalLayoutWidget_3.setFont(font)
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_42 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.horizontalLayout_3.addWidget(self.label_42)
        self.lineEdit_SaveResult = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEdit_SaveResult.setFont(font)
        self.lineEdit_SaveResult.setObjectName("lineEdit_SaveResult")
        self.horizontalLayout_3.addWidget(self.lineEdit_SaveResult)
        self.Button_SaveResultBrowse = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Button_SaveResultBrowse.setFont(font)
        self.Button_SaveResultBrowse.setObjectName("Button_SaveResultBrowse")
        self.horizontalLayout_3.addWidget(self.Button_SaveResultBrowse)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.pushButton_select = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_select.setGeometry(QtCore.QRect(560, 180, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.pushButton_select.setFont(font)
        self.pushButton_select.setObjectName("pushButton_select")
        self.label_select = QtWidgets.QLabel(self.tab_7)
        self.label_select.setGeometry(QtCore.QRect(740, 180, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_select.setFont(font)
        self.label_select.setObjectName("label_select")
        self.tabWidget.addTab(self.tab_7, "")
        self.label_light = QtWidgets.QLabel(self.centralwidget)
        self.label_light.setGeometry(QtCore.QRect(1480, 10, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_light.setFont(font)
        self.label_light.setStyleSheet(" QLabel {\n"
"                background-color: green;\n"
"                border-radius: 20px;  /* 圆角半径，设置为宽度的一半 */\n"
"                border: 2px solid darkgreen;  /* 边框 */\n"
"            }")
        self.label_light.setText("")
        self.label_light.setObjectName("label_light")
        self.Button_screenshot = QtWidgets.QPushButton(self.centralwidget)
        self.Button_screenshot.setEnabled(True)
        self.Button_screenshot.setGeometry(QtCore.QRect(40, 10, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_screenshot.setFont(font)
        self.Button_screenshot.setObjectName("Button_screenshot")
        self.label_savePath = QtWidgets.QLabel(self.centralwidget)
        self.label_savePath.setGeometry(QtCore.QRect(150, 10, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_savePath.setFont(font)
        self.label_savePath.setObjectName("label_savePath")
        self.lineEdit_savePath = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_savePath.setGeometry(QtCore.QRect(240, 10, 581, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_savePath.setFont(font)
        self.lineEdit_savePath.setObjectName("lineEdit_savePath")
        self.Button_browse = QtWidgets.QPushButton(self.centralwidget)
        self.Button_browse.setGeometry(QtCore.QRect(830, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_browse.setFont(font)
        self.Button_browse.setObjectName("Button_browse")
        self.Button_needleTemplate = QtWidgets.QPushButton(self.centralwidget)
        self.Button_needleTemplate.setGeometry(QtCore.QRect(990, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_needleTemplate.setFont(font)
        self.Button_needleTemplate.setObjectName("Button_needleTemplate")
        self.Checkbox_microAutoTrace = QtWidgets.QCheckBox(self.centralwidget)
        self.Checkbox_microAutoTrace.setGeometry(QtCore.QRect(1530, 10, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Checkbox_microAutoTrace.setFont(font)
        self.Checkbox_microAutoTrace.setObjectName("Checkbox_microAutoTrace")
        self.Button_padTemplate = QtWidgets.QPushButton(self.centralwidget)
        self.Button_padTemplate.setGeometry(QtCore.QRect(1150, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_padTemplate.setFont(font)
        self.Button_padTemplate.setObjectName("Button_padTemplate")
        self.Button_iuCalculate = QtWidgets.QPushButton(self.centralwidget)
        self.Button_iuCalculate.setGeometry(QtCore.QRect(1310, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_iuCalculate.setFont(font)
        self.Button_iuCalculate.setObjectName("Button_iuCalculate")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(200, 1040, 120, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "超低温探针台自动化控制软件 V1.05"))
        self.plainTextEdit_log.setPlaceholderText(_translate("MainWindow", "日志"))
        self.Button_needle1Stop.setText(_translate("MainWindow", "STOP"))
        self.label_4.setText(_translate("MainWindow", "Z dis"))
        self.label_3.setText(_translate("MainWindow", "X dis"))
        self.label_2.setText(_translate("MainWindow", "Y dis"))
        self.lineEdit_needle1Xdistance.setPlaceholderText(_translate("MainWindow", "30"))
        self.lineEdit_needle1Ydistance.setPlaceholderText(_translate("MainWindow", "30"))
        self.lineEdit_needle1Zdistance.setPlaceholderText(_translate("MainWindow", "30"))
        self.Button_needle1SetXdisConfirm.setText(_translate("MainWindow", "确认"))
        self.Button_needle1SetYdisConfirm.setText(_translate("MainWindow", "确认"))
        self.Button_needle1SetZdisConfirm.setText(_translate("MainWindow", "确认"))
        self.Button_pulling.setText(_translate("MainWindow", "抬升"))
        self.Button_pushing.setText(_translate("MainWindow", "按压"))
        self.label_needle1.setText(_translate("MainWindow", "探针位移"))
        self.label_needle1_2.setText(_translate("MainWindow", "连续移动步进"))
        self.label.setText(_translate("MainWindow", "显微镜位移"))
        self.label_6.setText(_translate("MainWindow", "实时检测"))
        self.label_10.setText(_translate("MainWindow", "计数值"))
        self.Button_SIM928.setText(_translate("MainWindow", "确认"))
        self.label_9.setText(_translate("MainWindow", "探针电压"))
        self.Button_SIM970.setText(_translate("MainWindow", "确认"))
        self.label_25.setText(_translate("MainWindow", "左上"))
        self.label_26.setText(_translate("MainWindow", "右上"))
        self.label_32.setText(_translate("MainWindow", "右下"))
        self.Button_Location1.setText(_translate("MainWindow", "确认"))
        self.Button_Location2.setText(_translate("MainWindow", "确认"))
        self.Button_Location3.setText(_translate("MainWindow", "确认"))
        self.label_35.setText(_translate("MainWindow", "行"))
        self.label_37.setText(_translate("MainWindow", "列"))
        self.Button_CreateMap.setText(_translate("MainWindow", "生成MAP"))
        self.Button_ContinueTest.setText(_translate("MainWindow", "继续测试"))
        self.Button_StopTest.setText(_translate("MainWindow", "停止测试"))
        self.Button_relay.setText(_translate("MainWindow", "光源开关"))
        self.Checkbox_ElecNeedle.setText(_translate("MainWindow", "探针"))
        self.Checkbox_Light.setText(_translate("MainWindow", "光纤"))
        self.label_23.setText(_translate("MainWindow", "X轴坐标"))
        self.label_24.setText(_translate("MainWindow", "Y轴坐标"))
        self.label_38.setText(_translate("MainWindow", "Z轴坐标"))
        self.label_39.setText(_translate("MainWindow", "按压点"))
        self.label_41.setText(_translate("MainWindow", "抬升点"))
        self.Button_PushLocation.setText(_translate("MainWindow", "确认"))
        self.Button_PullLocation.setText(_translate("MainWindow", "确认"))
        self.Button_PushBack.setText(_translate("MainWindow", "回到按压点"))
        self.Button_PullBack.setText(_translate("MainWindow", "回到抬升点"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "首页"))
        self.label_13.setText(_translate("MainWindow", "增益（初始为6.03）："))
        self.Button_cameraConfirm.setText(_translate("MainWindow", "确认"))
        self.label_14.setText(_translate("MainWindow", "帧率（初始为59.80）："))
        self.label_12.setText(_translate("MainWindow", "曝光（初始为5000）："))
        self.label_11.setText(_translate("MainWindow", "相机参数设置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "相机设置"))
        self.label_17.setText(_translate("MainWindow", "X轴移动距离（初始为0.5）："))
        self.label_18.setText(_translate("MainWindow", "Y轴移动距离（初始为0.5）："))
        self.pushButton_MicroConfirm.setText(_translate("MainWindow", "确认"))
        self.label_15.setText(_translate("MainWindow", "显微镜参数设置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "显微镜设置"))
        self.Button_needleSetConfirm.setText(_translate("MainWindow", "确认"))
        self.label_30.setText(_translate("MainWindow", "Z频率(初始为100)："))
        self.label_20.setText(_translate("MainWindow", "Z轴移动距离(初始为10，不得超过50)："))
        self.label_28.setText(_translate("MainWindow", "X频率(初始为100)："))
        self.label_22.setText(_translate("MainWindow", "Y电压(初始为100)："))
        self.label_19.setText(_translate("MainWindow", "Y轴移动距离(初始为30)："))
        self.label_27.setText(_translate("MainWindow", "Z电压(初始为100)："))
        self.label_29.setText(_translate("MainWindow", "Y频率(初始为100)："))
        self.label_16.setText(_translate("MainWindow", "X轴移动距离(初始为30)："))
        self.label_21.setText(_translate("MainWindow", "X电压(初始为100)："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "探针设置"))
        self.Button_relayConnect.setText(_translate("MainWindow", "连接"))
        self.label_microConnect.setText(_translate("MainWindow", "连接状态：未连接"))
        self.Button_SIM928Connect.setText(_translate("MainWindow", "连接"))
        self.Button_needleDisConnect.setText(_translate("MainWindow", "断开连接"))
        self.label_SIM928Connect.setText(_translate("MainWindow", "连接状态：未连接"))
        self.label_relayConnect.setText(_translate("MainWindow", "连接状态：未连接"))
        self.Button_SIM928DisConnect.setText(_translate("MainWindow", "断开连接"))
        self.label_36.setText(_translate("MainWindow", "请选择SIM970串口："))
        self.label_SIM970Connect.setText(_translate("MainWindow", "连接状态：未连接"))
        self.label_62.setText(_translate("MainWindow", "请选择继电器串口："))
        self.label_needleConnect.setText(_translate("MainWindow", "连接状态：未连接"))
        self.Button_needleConnect.setText(_translate("MainWindow", "连接"))
        self.label_31.setText(_translate("MainWindow", "请选择显微镜串口："))
        self.Button_relayDisConnect.setText(_translate("MainWindow", "断开连接"))
        self.Button_SIM970Connect.setText(_translate("MainWindow", "连接"))
        self.label_34.setText(_translate("MainWindow", "请选择Keithley2450串口："))
        self.Button_microDisConnect.setText(_translate("MainWindow", "断开连接"))
        self.label_33.setText(_translate("MainWindow", "请选择探针串口："))
        self.Button_SIM970DisConnect.setText(_translate("MainWindow", "断开连接"))
        self.Button_microConnect.setText(_translate("MainWindow", "连接"))
        self.GBIO_connect_button.setText(_translate("MainWindow", "扫描所有GBIO设备"))
        self.Serial_connect_refresh.setText(_translate("MainWindow", "刷新串口"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "串口设置"))
        self.label_40.setText(_translate("MainWindow", "导入的脚本路径："))
        self.lineEdit_Scripts.setPlaceholderText(_translate("MainWindow", "请选择脚本的路径"))
        self.Button_ScriptsBrowse.setText(_translate("MainWindow", "浏览"))
        self.textEdit_Scripts.setPlaceholderText(_translate("MainWindow", "脚本内容将在此处显示..."))
        self.Button_scriptConfirm.setText(_translate("MainWindow", "确认"))
        self.Button_scriptUpdate.setText(_translate("MainWindow", "修改"))
        self.label_42.setText(_translate("MainWindow", "保存结果的路径："))
        self.lineEdit_SaveResult.setPlaceholderText(_translate("MainWindow", "请选择要保存结果的路径"))
        self.Button_SaveResultBrowse.setText(_translate("MainWindow", "浏览"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "脚本输入"))
        self.pushButton_select.setText(_translate("MainWindow", "探针模板匹配"))
        self.label_select.setText(_translate("MainWindow", "当前选择：无"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "探针选择"))
        self.Button_screenshot.setText(_translate("MainWindow", "截图"))
        self.label_savePath.setText(_translate("MainWindow", "存储路径："))
        self.Button_browse.setText(_translate("MainWindow", "浏览"))
        self.Button_needleTemplate.setText(_translate("MainWindow", "探针模板匹配"))
        self.Checkbox_microAutoTrace.setText(_translate("MainWindow", "显微镜是否自动跟随"))
        self.Button_padTemplate.setText(_translate("MainWindow", "器件模板匹配"))
        self.Button_iuCalculate.setText(_translate("MainWindow", "电学性能测试"))

