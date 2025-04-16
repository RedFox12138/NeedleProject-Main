import threading
import time

from QTneedle.QTneedle.SerialLock import SerialLock


class LocationUpdater:
    x_distance = 0  # 初始x坐标
    y_distance = 0


    def __init__(self,anc):
        self.running = True
        self.timer = None
        self.anc = anc

    def update_location(self):
        if not self.running:
            return
        if(self.anc is not None):
            with SerialLock.serial_lock:
                self.getPosition()
                print("Updating location...")

        # 每 2 秒执行一次
        self.timer = threading.Timer(2, self.update_location)
        self.timer.start()

    def start(self):
        self.running = True
        self.update_location()  # 启动定时任务

    def stop(self):
        self.running = False
        if self.timer:
            self.timer.cancel()  # 取消定时任务

    def getPosition(self):
        try:
            # X轴坐标
            self.anc.write('[ch3:1]'.encode())
            time.sleep(0.2)

            self.anc.write('[v?]'.encode())
            self.anc.write('[read:pulse?]'.encode())
            ret = self.anc.readline()
            ret_str = ret.decode()
            start_index = ret_str.find('[+') + 2
            end_index = ret_str.find('v]')
            voltage_str = ret_str[start_index:end_index]
            distance = float(voltage_str)  # 浮点型
            x_distance = (1 - distance / 2.5) * 10.92 - 5
            time.sleep(0.1)

            self.anc.write('[ch2:1]'.encode())
            time.sleep(0.2)

            self.anc.write('[v?]'.encode())
            self.anc.write('[read:pulse?]'.encode())
            ret = self.anc.readline()
            ret_str = ret.decode()
            start_index = ret_str.find('[+') + 2
            end_index = ret_str.find('v]')
            voltage_str = ret_str[start_index:end_index]
            distance = float(voltage_str)  # 浮点型
            y_distance = (1 - distance / 2.5) * 10.92 - 5
            # ser4.write('[ch2:0]'.encode())
            time.sleep(0.1)

            self.anc.write('[ch2:0]'.encode())
            self.anc.write('[ch3:0]'.encode())

            LocationUpdater.x_distance = round(x_distance,4)
            LocationUpdater.y_distance = round(y_distance,4)
        except:
            print("位移器连接异常")

