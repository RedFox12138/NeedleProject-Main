import os
import sys
custom_lib_path = "c:\\users\\administrator\\appdata\\local\\programs\\python\\python37\\lib\\site-packages"

# 将路径添加到 sys.path
if custom_lib_path not in sys.path:
    sys.path.append(custom_lib_path)

import time
import datetime
from matplotlib import pyplot as plt
from scipy.optimize import fmin
import scipy.io as sio

from pymeasure.instruments.keithley import Keithley2450


def main():
    keithley = Keithley2450("USB0::0x05E6::0x2450::04595032::0::INSTR") # keithley2450地址
    keithley.reset() #keithley2450初始化sss
    time.sleep(0.1)

    #=================================================================================================
    #初始需修改的参数

    # sample_number = 'GQ1'   # 样品批号
    sample_number = 'GQ1'   # 样品批号

    Device_no = 'EB_1'
    V_max = 0.35  # IV扫描最大电压，单位：V
    V_step = 0.01  # 电压步进
    R_bias = 10070  # 偏置电阻大小

    #=================================================================================================

    I = [] # 电流
    V = [] # 电压

    V_set = [0]     # 实时设定电压
    V_add = 0       # 设定电压的初始值6

    #=================================================================================================
    # 获取扫描电压列表
    for i in range(4*int(V_max/V_step)):
        if i<int(V_max / V_step):
            V_add = V_add+V_step
            V_set.append(V_add)
        elif i<2*int(V_max / V_step):
            V_add = V_add-V_step
            V_set.append(V_add)
        elif i<3*int(V_max / V_step):
            V_add = V_add-V_step
            V_set.append(V_add)
        elif i<4*int(V_max / V_step):
            V_add = V_add+V_step
            V_set.append(V_add)
    # print(V_set) # 用来检查设定电压列表是否正确

    #==================================================================================================
    # 测量部分

    keithley.use_rear_terminals             #使用仪器前面端子
    keithley.wires
    keithley.apply_voltage()                # Sets up to source voltage
    keithley.compliance_current = 0.1       # Sets the compliance current
    keithley.auto_range_source()
    keithley.measure_current()              # Sets up to measure current

    keithley.enable_source()                #打开源表
    time.sleep(0.1)

    try:
        for i in range(len(V_set)):
            keithley.source_voltage = V_set[i]
            time.sleep(0.1)
            current = keithley.current
            I.append(current)
            V.append(V_set[i]-current*R_bias)
            print('此时的电流为=',current,'此时的电压为=',V_set[i],'此时的器件上电压为=',V_set[i]-current*R_bias)
        keithley.shutdown()
    except (KeyboardInterrupt,Exception) as e:
        print("已停止实时观测，关闭源表...")
        keithley.shutdown()


    time_str = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
    datapath = sys.argv[1]
    if not os.path.exists(datapath) :
        os.makedirs (datapath)
    fileName =sample_number +'_' +Device_no+'_Vmax_' + str(V_max) +'_Vstep_'+ str(V_step)+'_R_bias_'+ str(R_bias) +'_'+ time_str+'.mat'   # 保存的数据文件名称
    matFile = datapath +fileName
    print("保存路径是", matFile)
    sio.savemat(matFile, {'V_source_set' : V_set,'V': V,'I': I})

if __name__ == "__main__":
    sys.exit(main())
# plt.plot(V, I, 'b.')
# plt.grid(True)
# plt.xlabel('Voltage / V')
# plt.ylabel('Current / A')
# plt.show()