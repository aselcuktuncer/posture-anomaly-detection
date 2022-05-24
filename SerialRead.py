import serial
from time import sleep
from threading import Thread
from datetime import datetime


class ReadLine:
    def __init__(self, s):
        self.buf = bytearray()
        self.s = s

    def readline(self):
        i = self.buf.find(b"\n")
        if i >= 0:
            r = self.buf[:i + 1]
            self.buf = self.buf[i + 1:]
            return r
        while True:
            i = max(1, min(2048, self.s.in_waiting))
            data = self.s.read(i)
            i = data.find(b"\n")
            if i >= 0:
                r = self.buf + data[:i + 1]
                self.buf[0:] = data[i + 1:]
                return r
            else:
                self.buf.extend(data)




class Arduino:

    def __init__(self, ReadValue, Port="COM4", Error=None):
        # self.ser = serial.Serial(Port, 115200,timeout=None)
        #try:
        if Port == "COM7":
            self.ser = ReadLine(serial.Serial(Port, 115200, timeout=None))
        else:
            self.ser = ReadLine(serial.Serial(Port, 9600, timeout=None))
        """except IOError as a:
            print("Program stopped because of Serial Port Error")
            self.run = False
            return"""
        self.ReadValue = ReadValue
        self.error_count = 0
        self.error = self.error_func if Error == None else Error
        self.run = True
        self.thread = Thread(target=self.ReadSerial)
        self.thread.start()
        self.Port = Port
        

    def error_func(self, val):
        self.error_count += 1
        if self.error_count % 10 == 0:
            print("Error count: " + str(self.error_count))

    def ReadSerial(self):
        
        while self.run:
            
            try:
                
                val = self.ser.readline().decode('utf-8').strip()
                
                if val != '':
                    if val[0] == "!" and val[-1] == "#":
                        if self.Port == "COM5":
                            self.ReadValue("neck"+val[1:-1])
                        elif self.Port == "COM6":
                            self.ReadValue("back"+val[1:-1])
                        else:
                            self.ReadValue("textile"+val[1:-1])
                    else:
                        self.error_func(val)
                

            except IOError as a:
                print("Program stopped because of Serial Port Error")
                self.run = False
            except Exception as a:
                self.error_func("Char error")

    def Write(self,message):
        self.ser.s.write(message.encode('utf-8'))

    def __del__(self):
        self.run = False


