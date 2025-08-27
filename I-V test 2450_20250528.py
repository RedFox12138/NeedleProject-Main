import os
import sys
custom_lib_path = "c:\\users\\administrator\\appdata\\local\\programs\\python\\python37\\lib\\site-packages"

# 将路径添加到 sys.path
if custom_lib_path not in sys.path:
    sys.path.append(custom_lib_path)

import time
import datetime
import scipy.io

from pymeasure.instruments.keithley import Keithley2450

def main():
    keithley = Keithley2450("USB0::0x05E6::0x2450::04595034::0::INSTR") # keithley2450地址
    keithley.reset() #keithley2450初始化
    time.sleep(0.1)

    #=================================================================================================
    #初始需修改的参数

    Device_no = 'KR_1'
    V_max  = 1.3     # IV扫描最大电压，单位：V
    V_step = 0.5    # 电压步进
    R_bias = 99700      # 偏置电阻大小

    #=================================================================================================

    I = [] # 电流
    II=[]
    V = [] # 电压

    V_set = [0]     # 实时设定电压
    V_add = 0       # 设定电压的初始值

    #=================================================================================================
    # 获取扫描电压列表
    for i in range(4*int(V_max/V_step)):
        if (i<int(V_max/V_step)):
            V_add = V_add+V_step
            V_set.append(V_add)
        elif (i<2*int(V_max/V_step)):
            V_add = V_add-V_step
            V_set.append(V_add)
        elif (i<3*int(V_max/V_step)):
            V_add = V_add-V_step
            V_set.append(V_add)
        elif (i<4*int(V_max/V_step)):
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

    # keithley.use_rear_terminals             #使用仪器前面端子
    # keithley.wires
    # keithley.apply_current()                # Sets up to source voltage
    # keithley.compliance_voltage = 15       # Sets the compliance current
    # keithley.auto_range_source()
    # keithley.measure_voltage()              # Sets up to measure current

    # keithley.enable_source()                #打开源表
    # time.sleep(0.1)
    # print(keithley.voltage)

    for i in range(len(V_set)):
        keithley.source_voltage = V_set[i]
        time.sleep(0.1)
        current = keithley.current
        I.append(current)
        V.append(V_set[i]-current*R_bias)
        II.append(current-(V_set[i]-current*R_bias)/R_bias)
        print( 'V_set=',V_set[i], '  V=',V_set[i]-current*R_bias,' I=',current)
        time.sleep(0.1)


    keithley.shutdown()                     # Ramps the current to 0 mA and disables output
    keithley.reset() #keithley2450初始化
    time.sleep(0.1)

    #=================================================================================================================
    #保存文件为matlab格式

    last_time = time.time()
    time_str = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')

    # datapath = 'E:\\WL\\IV_test\\20250528hole_2450\\'                  # 数据文件夹目录

    datapath = sys.argv[0]
    print("保存路径是", datapath)
    if not os.path.exists(datapath):
        os.makedirs(datapath)
    fileName = Device_no + '_Vmax_' + str(V_max) + '_Vstep_' + str(V_step) + '_R_bias_' + str(
        R_bias) + '_' + time_str + '.mat'  # 保存的数据文件名称
    matFile = datapath + fileName
    print("保存路径是", matFile)
    scipy.io.savemat(matFile, {'V_source_set': V_set, 'V': V, 'I': I})

    # plt.plot(V, I, 'b.')
    # plt.grid(True)
    # plt.xlabel('Voltage / V')
    # plt.ylabel('Current / A')
    # plt.show()

if __name__ == "__main__":
    sys.exit(main())

