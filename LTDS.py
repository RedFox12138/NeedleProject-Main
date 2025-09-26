import importlib
import sys
import time

import MainPage
from ANC300 import Positioner
import math

from QTneedle.QTneedle.Position import getPosition
from QTneedle.QTneedle.SerialLock import SerialLock
from QTneedle.QTneedle.locationClass import locationClass
from SerialPage import NeedelConnectionThread, SIM928ConnectionThread
from StopClass import StopClass

ax = {'x':1,'y':2,'z':3,'x2':4,'y2':5,'z2':6}
def ReturnNeedleMove(direction,distance,indicatorLight,isclick=False,flag=False,equipment=0):
    xyForLowTemp = '2000'
    xyForhighTemp = '300'
    zForLowTemp = '500'
    zForhighTemp = '100'

    frequencyXY = xyForLowTemp
    frequencyZ = zForLowTemp

    voltageForhighTemp = '100'
    voltageForlowTemp = '200'

    directionArray = [[2,3,1],[6,5,4]]
    with SerialLock.serial_lock:
        try:
            anc = NeedelConnectionThread.anc
            indicatorLight.setStyleSheet(MainPage.MainPage1.get_stylesheet(True))
            if direction == 0:
                anc.write( ('[ch'+ str(directionArray[equipment][0])+':1]').encode())
                anc.write('[cap:013nF]'.encode())
                anc.write(('[volt:+'+voltageForlowTemp+'V]').encode())
                anc.write(('[freq:+0'+frequencyXY+'Hz]').encode())
                anc.write(('[-:0000' + str(distance) + '] ').encode())  # +-方向
            elif direction == 1:
                anc.write( ('[ch'+ str(directionArray[equipment][0])+':1]').encode())
                anc.write('[cap:013nF]'.encode())
                anc.write(('[volt:+'+voltageForlowTemp+'V]').encode())
                anc.write(('[freq:+0'+frequencyXY+'Hz]').encode())
                anc.write(('[+:0000' + str(distance) + '] ').encode())  # +-方向
            elif direction == 2:
                anc.write( ('[ch'+ str(directionArray[equipment][1])+':1]').encode())
                anc.write('[cap:013nF]'.encode())
                anc.write(('[volt:+'+voltageForlowTemp+'V]').encode())
                anc.write(('[freq:+0'+frequencyXY+'Hz]').encode())
                if equipment==1:
                    anc.write(('[+:0000' + str(distance) + '] ').encode())  # +-方向
                else :
                    anc.write(('[-:0000' + str(distance) + '] ').encode())  # +-方向

            elif direction ==3 :
                anc.write( ('[ch'+ str(directionArray[equipment][1])+':1]').encode())
                anc.write('[cap:013nF]'.encode())
                anc.write(('[volt:+'+voltageForlowTemp+'V]').encode())
                anc.write(('[freq:+0'+frequencyXY+'Hz]').encode())
                if equipment==1:
                    anc.write(('[-:0000' + str(distance) + '] ').encode())  # +-方向
                else :
                    anc.write(('[+:0000' + str(distance) + '] ').encode())  # +-方向
            elif direction == 4 :
                anc.write(('[ch'+ str(directionArray[equipment][2])+':1]').encode())
                anc.write('[cap:013nF]'.encode())
                anc.write(('[volt:+'+voltageForlowTemp+'V]').encode())
                anc.write(('[freq:+00'+frequencyZ+'Hz]').encode())
                anc.write(('[-:0000' + str(distance) + '] ').encode())  # +-方向
            elif direction == 5:
                anc.write( ('[ch'+ str(directionArray[equipment][2])+':1]').encode())
                anc.write('[cap:013nF]'.encode())
                anc.write(('[volt:+'+voltageForlowTemp+'V]').encode())
                anc.write(('[freq:+00'+frequencyZ+'Hz]').encode())
                anc.write(('[+:0000' + str(distance) + '] ').encode())  # +-方向
            if flag:
                time.sleep((distance + 1) / 300)
            else:
                time.sleep(0.8)

            if not isclick:
                indicatorLight.setStyleSheet(MainPage.MainPage1.get_stylesheet(False))
        except (AttributeError, ValueError):
            print("请检查探针是否连接")


def WhileMove(direction,indicatorLight,equipment=0,distance=1000):
    xyForLowTemp = '2000'
    xyForhighTemp = '300'
    zForLowTemp = '1000'
    zForhighTemp = '500'
    voltageForhighTemp = '100'
    voltageForlowTemp = '200'

    frequencyXY = xyForLowTemp
    frequencyZ = zForLowTemp



    directionArray = [[2,3,1],[6,5,4]]
    with SerialLock.serial_lock:
        indicatorLight.setStyleSheet(MainPage.MainPage1.get_stylesheet(True))
        anc = NeedelConnectionThread.anc
        anc.write('[ch1:0]'.encode())
        anc.write('[ch2:0]'.encode())
        anc.write('[ch3:0]'.encode())
        anc.write('[ch4:0]'.encode())
        anc.write('[ch5:0]'.encode())
        anc.write('[ch6:0]'.encode())
        time.sleep(0.1)
        # distance = min(1000,distance)
        if direction == 0 or direction == 1:
            anc.write( ('[ch'+ str(directionArray[equipment][0])+':1]').encode())
            anc.write('[cap:013nF]'.encode())
            anc.write(('[volt:+'+voltageForlowTemp+'V]').encode())
            anc.write(('[freq:+0'+frequencyXY+'Hz]').encode())
            time.sleep(0.1)
            num_str = '[-:0000' if direction ==0 else '[+:0000'
            while StopClass.stop_num == 0:
                anc.write((num_str + str(distance) + '] ').encode())  # +-方向
                time.sleep(0.1)
        elif direction == 2 or direction == 3:
            anc.write( ('[ch'+ str(directionArray[equipment][1])+':1]').encode())
            anc.write('[cap:013nF]'.encode())
            anc.write(('[volt:+'+voltageForlowTemp+'V]').encode())
            anc.write(('[freq:+0'+frequencyXY+'Hz]').encode())
            time.sleep(0.1)
            num_str1 = '[+:0000' if direction == 2 else '[-:0000'
            num_str2 = '[-:0000' if direction == 2 else '[+:0000'
            while StopClass.stop_num == 0:
                if equipment==1:
                    anc.write((num_str1 + str(distance) + '] ').encode())  # +-方向
                else :
                    anc.write((num_str2 + str(distance) + '] ').encode())  # +-方向
                time.sleep(0.1)
        #Z轴, 4按压,5抬升
        elif  direction == 4 or direction == 5:
            anc.write(('[ch' + str(directionArray[equipment][2]) + ':1]').encode())
            anc.write('[cap:013nF]'.encode())
            anc.write(('[volt:+'+voltageForlowTemp+'V]').encode())
            anc.write(('[freq:+0'+frequencyZ+'Hz]').encode())
            time.sleep(0.2)
            num_str = '[+:0000' if direction == 4 else '[-:0000'
            while StopClass.stop_num == 0:
                anc.write((num_str + str(distance) + '] ').encode())  # +-方向
                time.sleep(0.2)
                keithley = SIM928ConnectionThread.anc
                current = keithley.current
                print(current)


        StopClass.stop_num = 0
        locationClass.locationX, locationClass.locationY, locationClass.locationZ = getPosition()
        indicatorLight.setStyleSheet(MainPage.MainPage1.get_stylesheet(False))

def voltage_and_frequency(xv,yv,xf,yf):
    anc = NeedelConnectionThread.anc
    anc.setv(ax['x'], xv)
    anc.setv(ax['y'], yv)
    anc.setf(ax['x'], xf)
    anc.setf(ax['y'], yf)



