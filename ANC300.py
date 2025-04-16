"""
Created on Fri Oct 29 2021

@author: liu
"""

import pyvisa

class Positioner(object):
    def __init__(self, visa_name):
        rm = pyvisa.ResourceManager()
        self.pyvisa = rm.open_resource(visa_name)
#        self.pyvisa.timeout = 10000
  
    def write(self, string):
        self.pyvisa.write(string)
        
    def print(self, string):
        self.pyvisa.print(string)
        
    def setf(self, AID, FRQ):
        write_str = 'setf %d %d' % (AID,FRQ)
        #print(write_str)
        self.write(write_str) 

    def setm(self, AID, AMODE):
        #AMODE can select 'gnd' 'inp' 'cap' 'stp' 'off' 'stp+' or 'stp-'
        write_str = 'setm %d %s' % (AID,AMODE)
        #print(write_str)
        self.write(write_str) 
                
    def setv(self, AID, VOL):
        write_str = 'setv %d %.1f' % (AID,VOL)
        #pri1nt(write_str)
        self.write(write_str) 

    def seta(self, AID, VOL):
        write_str = 'seta %d %.1f' % (AID,VOL)
        #print(write_str)
        self.write(write_str) 

    #set status of AC-IN input
    def setaci(self, AID, switch): 
        write_str = 'setaci %d %s' % (AID,switch)
        #switch can select 'on' and 'off'
        #print(write_str)
        self.write(write_str) 

    #set status of DC-IN input
    def setdci(self, AID, switch): 
        write_str = 'setdci %d %s' % (AID,switch)
        #switch can select 'on' or 'off'
        #print(write_str)
        self.write(write_str)        
        
    def stepu(self, AID, C):
        write_str = 'stepu %d %d' % (AID,C)
        print(write_str)
        self.write(write_str) 

    def stepd(self, AID, C):
        write_str = 'stepd %d %d' % (AID,C)
        print(write_str)
        self.write(write_str)

    def close(self):
        if self.pyvisa is not None:
            try:
                self.pyvisa.close()
            except Exception as e:
                print(f"Error closing pyvisa resource: {e}")
            finally:
                self.pyvisa = None