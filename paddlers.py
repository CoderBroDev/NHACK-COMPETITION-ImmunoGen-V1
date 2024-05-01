import serial
from time import sleep
from servo import Servo  # Assuming you have a Servo class implementation

bttx = 9  # tx of bluetooth module is connected to pin 9 of arduino
btrx = 10  # rx of bluetooth module is connected to pin 10 of arduino

bluetooth = serial.Serial('/dev/ttyS0', 9600)  # Change '/dev/ttyS0' to your serial port
x = Servo(11)  # Servo is connected to pin 11 of arduino

while True:
    if bluetooth.in_waiting > 0:  # if bluetooth module is transmitting data
        pos = int(bluetooth.read())  # store the data in pos variable
        print(pos)
        x.write(pos)  # move servo head to the given position
        sleep(0.1)# to stabilize
