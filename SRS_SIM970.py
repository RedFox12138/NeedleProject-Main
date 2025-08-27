# -*- coding: utf-8 -*-
"""
    Created on Mon Jul 24 13:32:31 2017

    @author: rise
"""

import pyvisa
import numpy as np
import time


class SRSSIM970(object):
    """
        Python class for SRS SIM970 multi-meters inside a SIM900
        mainframe
    """
    def __init__(self, sim900port, visa_name):
        rm = pyvisa.ResourceManager()
        self.pyvisa = rm.open_resource(visa_name)
        
        #self.pyvisa.timeout = 5000 # Set response timeout (in milliseconds)
        # self.pyvisa.query_delay = 1 # Set extra delay time between write and read commands
        
        write_str = 'conn'+str(sim900port)+",'quit_vol'"
        self.pyvisa.write(write_str)
        self.sim900port = sim900port
        # Anything else here that needs to happen on initialization

    def read(self):
        return self.pyvisa.read()
    
    
    def read_n_return_mean_std(self,Ch,n):
        data = []
        write_str = 'VOLT?'+Ch+','+str(n)
        self.write(write_str)

        for i in range(n):
            a = self.pyvisa.read()
            time.sleep(0.001)
            data.append(float(a))
            
        data_mean = np.mean(data)
        data_std = np.std(data)
        
        return data,data_mean, data_std
    
    def write(self, string):
        self.pyvisa.write(string)
        

    def query(self, string):
        return self.pyvisa.query(string)
    
    def write_simport(self, message):
        write_str = 'SNDT ' + str(self.sim900port) + ',\"' + message + '\"'
        # print write_str
        self.write(write_str) # Format of 'SNDT 4,\"GAIN 10\"'
    
    def get_simport(self, message,i):
        write_str = 'SNDT ' + str(self.sim900port) + ',\"' + message + '\"'
#        get_str = 'GETN' + str(self.sim900port) + '800'
        return self.query(write_str) # Format of 'SNDT 4,\"GAIN 10\"'
    
#    def measure(self, channel, i):
        
    
    def reset(self):
        self.write_simport('*RST')

    
    def quit_vol(self):
        self.pyvisa.write('quit_vol') 
       
