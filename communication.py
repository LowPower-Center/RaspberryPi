import serial    #import serial module
import time

# Serial port
class port_communicate():
    def __init__(self):
        try:
            self.ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # open named port at 9600,1s timeot
        except:
            self.ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)
    def forward(self,delay):
        self.ser.write(b'f')
        time.sleep(delay)
        self.ser.write(b'0')

    def backward(self,delay):
        self.ser.write(b'b')
        time.sleep(delay)
        self.ser.write(b'0')
    def left(self,delay):
        self.ser.write(b'l')
        time.sleep(delay)
        self.ser.write(b'0')
    def right(self,delay):
        self.ser.write(b'r')
        time.sleep(delay)
        self.ser.write(b'0')
    def stop(self):
        self.ser.write(b'0')
    def response(self):
        self.response = self.ser.readall()
        return self.response
    def close(self):
        self.ser.close()
    def publish_mission(self,mission_number):
        self.ser.write('{}'.format(mission_number).encode())
    def send_chracter(self,character):
        self.ser.write(character.encode())

