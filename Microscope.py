# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 14:09:54 2024

@author: Administrator
"""
import zauxdllPython
from SerialPage import SerialConnectionThread


# import Micro.zauxdllPython

zaux = None

def ReturnZauxdll(direction,distance):

    try:
        global zaux
        if zaux is None :
            zaux = zauxdllPython.ZMCWrapper()
            zaux.connectcom(SerialConnectionThread.port_com)

            zaux.set_atype(0, 1)
            zaux.set_units(0, 10000)
            zaux.set_accel(0, 1000)
            zaux.set_decel(0, 10)
            zaux.set_speed(0, 1000)

            zaux.get_atype(0)
            zaux.get_untis(0)
            zaux.get_accel(0)
            zaux.get_decel(0)
            zaux.get_speed(0)
        # zaux = zauxdllPython.ZMCWrapper()
        # zaux.connect(SerialConnectionThread.port_ip)




        zaux.move(direction, distance)
        # zaux.disconnect()


    except (AttributeError, ValueError):
        print("请检查显微镜是否连接")
    # zaux.disconnect()
