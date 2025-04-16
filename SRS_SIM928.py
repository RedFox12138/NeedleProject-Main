import sys
# 定义你要添加的库文件路径
custom_lib_path = "c:\\users\\administrator\\appdata\\local\\programs\\python\\python37\\lib\\site-packages"

# 将路径添加到 sys.path
if custom_lib_path not in sys.path:
    sys.path.append(custom_lib_path)
import pyvisa

class SIM928(object):
    """Python class for SRS SIM928 Isolated Voltage Source inside a SIM900
    mainframe, written by Adam McCaughan"""
    def __init__(self, sim900port, visa_name):
        
        rm = pyvisa.ResourceManager()
        self.pyvisa = rm.open_resource(visa_name)
        
        self.pyvisa.timeout = 5000 # Set response timeout (in milliseconds)
        # self.pyvisa.query_delay = 1 # Set extra delay time between write and read commands
        
#        write_str = 'conn'+str(sim900port)+",'quit_source'"
#        self.pyvisa.write(write_str)
        self.sim900port = sim900port
        # Anything else here that needs to happen on initialization

    def read(self):
        return self.pyvisa.read()
    
    def write(self, string):
        self.pyvisa.write(string)
    
    def query(self, string):
        return self.pyvisa.query(string)

    def write_simport(self, message):
        write_str = 'SNDT ' + str(self.sim900port) + ',\"' + message + '\"'
        # print write_str
        self.write(write_str) # Format of 'SNDT 4,\"GAIN 10\"'
    
    def ask_simport(self, message):
        write_str = 'SNDT ' + str(self.sim900port) + ',\"' + message + '\"'
        return self.query(write_str) # Format of 'SNDT 4,\"GAIN 10\"'
    
    def reset(self):
        self.write_simport('*RST')
        
    def set_voltage(self, voltage=0.0):
        # In a string, %0.4e converts a number to scientific notation
        self.write_simport('VOLT %0.4e' %(voltage))
    def set_output(self, output=False):
        if output==True:
            self.write_simport('OPON') 
        else:
            self.write_simport('OPOF')  # Only uses "OPOF" or "OPON": "OPOFF" does not work

    def quit_source(self):
        self.write('quit_source')
