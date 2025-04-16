import time
from tkinter import messagebox
import tkinter as tk


from QTneedle.QTneedle.SerialLock import SerialLock
from SerialPage import NeedelConnectionThread
import sys

from StopClass import StopClass

# 定义你要添加的库文件路径
custom_lib_path = "c:\\users\\administrator\\appdata\\local\\programs\\python\\python37\\lib\\site-packages"

# 将路径添加到 sys.path
if custom_lib_path not in sys.path:
    sys.path.append(custom_lib_path)

def getPosition(Z_flag=False):
    anc = NeedelConnectionThread.anc
    x_distance = 0
    y_distance = 0

    if(Z_flag is not True):
        # X轴坐标
        anc.write('[ch3:1]'.encode())
        time.sleep(0.2)
        anc.write('[v?]'.encode())
        anc.write('[read:pulse?]'.encode())
        ret = anc.readline()
        ret_str = ret.decode()
        start_index = ret_str.find('[+') + 2
        end_index = ret_str.find('v]')
        voltage_str = ret_str[start_index:end_index]
        distance = float(voltage_str)  # 浮点型
        x_distance = (1 - distance / 2.5) * 10.92 - 5
        time.sleep(0.1)

        anc.write('[ch2:1]'.encode())
        time.sleep(0.2)
        anc.write('[v?]'.encode())
        anc.write('[read:pulse?]'.encode())
        ret = anc.readline()
        ret_str = ret.decode()
        start_index = ret_str.find('[+') + 2
        end_index = ret_str.find('v]')
        voltage_str = ret_str[start_index:end_index]
        distance = float(voltage_str)  # 浮点型
        y_distance = (1 - distance / 2.5) * 10.92 - 5
        time.sleep(0.1)

    anc.write('[ch1:1]'.encode())
    time.sleep(0.2)
    anc.write('[v?]'.encode())
    anc.write('[read:pulse?]'.encode())
    ret = anc.readline()
    ret_str = ret.decode()
    start_index = ret_str.find('[+') + 2
    end_index = ret_str.find('v]')
    voltage_str = ret_str[start_index:end_index]
    distance = float(voltage_str)  # 浮点型
    z_distance = (1 - distance / 2.5) * 10.92 - 5
    time.sleep(0.1)

    anc.write('[ch1:0]'.encode())
    anc.write('[ch2:0]'.encode())
    anc.write('[ch3:0]'.encode())
    return round(x_distance,4),round(y_distance,4),round(z_distance,6)

def move_to_Z(z):
    with SerialLock.serial_lock:
        _,_,z_current = getPosition(True)

    while (abs(z_current - z) > 0.0003) :
        if (StopClass.stop_num == 1):
            break
        flag = False
        step_per_unit = 0.06  # 假设每 0.06 单位对应 100 步
        with SerialLock.serial_lock:
            z_diff = round((z - z_current), 3)
            if z_diff > 0:
                move('-Z', abs(z_diff) / step_per_unit * 500, flag)
            elif z_diff < 0:
                move('Z', abs(z_diff) / step_per_unit * 500, flag)
            _,_,z_current = getPosition(True)
    StopClass.stop_num =0
    return z_current


def move_to_target(x, y):
    with SerialLock.serial_lock:
        x_current, y_current,_ = getPosition()
        x_diff = round((x - x_current), 3)
        y_diff = round((y - y_current), 3)
        flag = True
        if (x_diff > 0):
            move('X', abs(x_diff) / 0.03 * 1000, flag)
        elif (x_diff < 0):
            move('-X', abs(x_diff) / 0.03 * 1000, flag)

        if (y_diff > 0):
            move('Y', abs(y_diff) / 0.03 * 1000, flag)
        elif (y_diff < 0):
            move('-Y', abs(y_diff) / 0.03 * 1000, flag)
        x_current, y_current,_ = getPosition()
    while ( (abs(y_current - y) > 0.003 or abs(x_current - x) > 0.003)):
        if(StopClass.stop_num==1):
            StopClass.stop_num=0
            anc = NeedelConnectionThread.anc
            anc.write('[ch1:1]'.encode())
            anc.write('[cap:000nF]'.encode())
            anc.write('[volt:+000V] '.encode())
            anc.write('[freq:+00000Hz]'.encode())
            time.sleep(0.2)
            anc.write('[ch2:1]'.encode())
            anc.write('[cap:000nF]'.encode())
            anc.write('[volt:+000V] '.encode())
            anc.write('[freq:+00000Hz]'.encode())
            time.sleep(0.2)
            anc.write('[ch3:1]'.encode())
            anc.write('[cap:000nF]'.encode())
            anc.write('[volt:+000V] '.encode())
            anc.write('[freq:+00000Hz]'.encode())
            time.sleep(0.2)
            anc.write('[ch1:0]'.encode())
            anc.write('[ch2:0]'.encode())
            anc.write('[ch3:0]'.encode())
            time.sleep(0.2)
            break
        else:
            flag = False
            step_per_unit = 0.06  # 假设每 0.06 单位对应 100 步
            with SerialLock.serial_lock:
                x_diff = round((x - x_current), 3)
                y_diff = round((y - y_current), 3)
                if x_diff > 0:
                    move('X', abs(x_diff) / step_per_unit * 1000, flag)
                elif x_diff < 0:
                    move('-X', abs(x_diff) / step_per_unit * 1000, flag)
                if y_diff > 0:
                    move('Y', abs(y_diff) / step_per_unit * 1000, flag)
                elif y_diff < 0:
                    move('-Y', abs(y_diff) / step_per_unit * 1000, flag)
                x_current, y_current,_ = getPosition()
    return x_current, y_current

def move(axis,distance,flag):
    ser4 = NeedelConnectionThread.anc
    if(axis == '-X'):
        ser4.write('[ch3:1]'.encode())
        ser4.write('[cap:013nF]'.encode())
        ser4.write('[volt:+200V] '.encode())
        ser4.write('[freq:+00500Hz]'.encode())
        ser4.write(('[+:0000' + str(distance) + '] ').encode())  # +-方向
    elif(axis == 'X'):
        ser4.write('[ch3:1]'.encode())
        ser4.write('[cap:013nF]'.encode())
        ser4.write('[volt:+200V] '.encode())
        ser4.write('[freq:+00500Hz]'.encode())
        ser4.write(('[-:0000' + str(distance) + '] ').encode())  # +-方向
    elif(axis == '-Y'):
        ser4.write('[ch2:1]'.encode())
        ser4.write('[cap:013nF]'.encode())
        ser4.write('[volt:+200V] '.encode())
        ser4.write('[freq:+00500Hz]'.encode())
        ser4.write(('[+:0000' + str(distance) + '] ').encode())  # +-方向
    elif(axis == 'Y'):
        ser4.write('[ch2:1]'.encode())
        ser4.write('[cap:013nF]'.encode())
        ser4.write('[volt:+200V] '.encode())
        ser4.write('[freq:+00500Hz]'.encode())
        ser4.write(('[-:0000' + str(distance) + '] ').encode())  # +-方向
    elif(axis == 'Z'):
        ser4.write('[ch1:1]'.encode())
        ser4.write('[cap:013nF]'.encode())
        ser4.write('[volt:+200V] '.encode())
        ser4.write('[freq:+00500Hz]'.encode())
        ser4.write(('[+:0000' + str(distance) + '] ').encode())  # +-方向
    elif(axis == '-Z'):
        ser4.write('[ch1:1]'.encode())
        ser4.write('[cap:013nF]'.encode())
        ser4.write('[volt:+200V] '.encode())
        ser4.write('[freq:+00500Hz]'.encode())
        ser4.write(('[-:0000' + str(distance) + '] ').encode())  # +-方向

    if(flag):
        time.sleep((distance+1)/1000)
    else:
        time.sleep(0.3)

    # ser4.write('[ch1:0]'.encode())
    # ser4.write('[ch2:0]'.encode())
    # ser4.write('[ch3:0]'.encode())