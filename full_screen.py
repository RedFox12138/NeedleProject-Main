from PyQt5.QtWidgets import QDesktopWidget


def show_custom_fullscreen(window):
    # 获取屏幕尺寸
    screen_geometry = QDesktopWidget().screenGeometry()
    # 设置窗口大小为屏幕尺寸
    window.setGeometry(screen_geometry)
    # 显示窗口
    window.show()