import time
from tkinter import messagebox
import tkinter as tk


from QTneedle.QTneedle.SerialLock import SerialLock
from SerialPage import NeedelConnectionThread, SIM928ConnectionThread
import sys

from StopClass import StopClass

# 定义你要添加的库文件路径
custom_lib_path = "c:\\users\\administrator\\appdata\\local\\programs\\python\\python37\\lib\\site-packages"

# 将路径添加到 sys.path
if custom_lib_path not in sys.path:
    sys.path.append(custom_lib_path)

def getPosition(Z_flag=False,Only_XY=False):

    anc = NeedelConnectionThread.anc
    x_distance = 0
    y_distance = 0
    z_distance = 0

    if Z_flag is not True:
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

    if Only_XY is not True:
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

    # anc.write('[ch1:0]'.encode())
    # anc.write('[ch2:0]'.encode())
    # anc.write('[ch3:0]'.encode())

    return round(x_distance,4),round(y_distance,4),round(z_distance,6)

def move_to_Z(z,Voltage_flag=False):
    with SerialLock.serial_lock:
        _,_,z_current = getPosition(Z_flag=True)

    #低温情况下abs(z_current - z)应该是0.001，常温情况是0.005
    while (abs(z_current - z) > 0.001) :
        # 低温情况下Z_k应该是500，常温情况是0.1
        Z_k = 500
        if(Voltage_flag==True):
            keithley = SIM928ConnectionThread.anc
            current = keithley.current
            print(current)
            if current>= 9e-10:
                break
        if (StopClass.stop_num == 1):
            break
        flag = False

        # 低温情况下step_per_unit是0.06，常温情况是0.12
        step_per_unit = 0.06
        with SerialLock.serial_lock:
            z_diff = round((z - z_current), 3)
            if z_diff > 0:
                move('-Z', abs(z_diff) / step_per_unit * Z_k, flag)
            elif z_diff < 0:
                move('Z', abs(z_diff) / step_per_unit * Z_k, flag)
            _,_,z_current = getPosition(Z_flag=True)
    StopClass.stop_num =0
    return z_current


def move_to_target(x, y):
    # 低温情况下XY_k是1000，常温情况是100
    XY_k = 1000
    XY_k_2 = 10000
    step_per_unit = 0.06  # 假设每 0.06 单位对应 100 步
    with SerialLock.serial_lock:
        x_current, y_current,_ = getPosition(Only_XY=True)
        x_diff = round((x - x_current), 3)
        y_diff = round((y - y_current), 3)
        flag = True
        if (x_diff > 0):
            move('X', abs(x_diff) / 0.03 * XY_k, flag)
        elif (x_diff < 0):
            move('-X', abs(x_diff) / 0.03 * XY_k, flag)

        if (y_diff > 0):
            move('Y', abs(y_diff) / 0.03 * XY_k, flag)
        elif (y_diff < 0):
            move('-Y', abs(y_diff) / 0.03 * XY_k, flag)
        x_current, y_current,_ = getPosition(Only_XY=True)


    while  abs(y_current - y) > 0.003 :
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
            with SerialLock.serial_lock:
                y_diff = round((y - y_current), 3)
                if y_diff > 0:
                    move('Y', abs(y_diff) / step_per_unit * XY_k_2, flag)
                elif y_diff < 0:
                    move('-Y', abs(y_diff) / step_per_unit * XY_k_2, flag)
                _, y_current,_ = getPosition(Only_XY=True)
    while abs(x_current - x) > 0.003:
        if(StopClass.stop_num == 1):
            StopClass.stop_num = 0
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
            with SerialLock.serial_lock:
                x_diff = round((x - x_current), 3)
                if x_diff > 0:
                    move('X', abs(x_diff) / step_per_unit * XY_k_2, flag)
                elif x_diff < 0:
                    move('-X', abs(x_diff) / step_per_unit * XY_k_2, flag)
                x_current, _, _ = getPosition(Only_XY=True)

    return x_current, y_current



def move(axis,distance,flag):
    # 移动时间，低温下是0.3，常温下是0.1
    move_time = 0.5
    ser4 = NeedelConnectionThread.anc
    if(axis == '-X'):
        ser4.write('[ch3:1]'.encode())
        ser4.write('[cap:013nF]'.encode())
        ser4.write('[volt:+200V] '.encode())
        ser4.write('[freq:+5000Hz]'.encode())
        ser4.write(('[+:0000' + str(distance) + '] ').encode())  # +-方向
    elif(axis == 'X'):
        ser4.write('[ch3:1]'.encode())
        ser4.write('[cap:013nF]'.encode())
        ser4.write('[volt:+200V] '.encode())
        ser4.write('[freq:+5000Hz]'.encode())
        ser4.write(('[-:0000' + str(distance) + '] ').encode())  # +-方向
    elif(axis == '-Y'):
        ser4.write('[ch2:1]'.encode())
        ser4.write('[cap:013nF]'.encode())
        ser4.write('[volt:+200V] '.encode())
        ser4.write('[freq:+5000Hz]'.encode())
        ser4.write(('[+:0000' + str(distance) + '] ').encode())  # +-方向
    elif(axis == 'Y'):
        ser4.write('[ch2:1]'.encode())
        ser4.write('[cap:013nF]'.encode())
        ser4.write('[volt:+200V] '.encode())
        ser4.write('[freq:+5000Hz]'.encode())
        ser4.write(('[-:0000' + str(distance) + '] ').encode())  # +-方向
    elif(axis == 'Z'):
        ser4.write('[ch1:1]'.encode())
        ser4.write('[cap:013nF]'.encode())
        ser4.write('[volt:+200V] '.encode())
        ser4.write('[freq:+0500Hz]'.encode())
        ser4.write(('[+:0000' + str(distance) + '] ').encode())  # +-方向
    elif(axis == '-Z'):
        ser4.write('[ch1:1]'.encode())
        ser4.write('[cap:013nF]'.encode())
        ser4.write('[volt:+200V] '.encode())
        ser4.write('[freq:+0500Hz]'.encode())
        ser4.write(('[-:0000' + str(distance) + '] ').encode())  # +-方向

    if(flag):
        time.sleep((distance+1)/1000)
    else:
        time.sleep(move_time)

    # ser4.write('[ch1:0]'.encode())
    # ser4.write('[ch2:0]'.encode())
    # ser4.write('[ch3:0]'.encode())