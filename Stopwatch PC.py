from pynput.keyboard import Key, Controller
from pynput.keyboard import Key, Listener

keyboard = Controller()


import serial
import time

# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM3', 9800, timeout=1)
time.sleep(2)



def start():
    t = 0
    num=0
    while t == 0:
        line = ser.readline()   # read a byte
        if line:
            string = line.decode()  # convert the byte string to a unicode string
            num = int(string) # convert the unicode string to an int
            t = num
        if t > 90:
            keyboard.press(Key.space)
            keyboard.release(Key.space)


def main():
    c=0
    num2 = 0 
    i = 1
    num=0
    while i < 6:
        line = ser.readline()   # read a byte
        if line:
            string = line.decode()  # convert the byte string to a unicode string
            num = int(string) # convert the unicode string to an int
            print(num)
            while num < 250:
                line = ser.readline()   # read a byte
                if line:
                    string = line.decode()  # convert the byte string to a unicode string
                    num = int(string) # convert the unicode string to an int
                    print(num)
                    c=1

        while num > 300 and c==1:

            keyboard.press(Key.enter)
            keyboard.release(Key.enter)


            line = ser.readline()   # read a byte
            if line:
                string = line.decode()  # convert the byte string to a unicode string
                num = int(string) # convert the unicode string to an int
                print(num)
                c=0
try:
    start()
except:
    start()
try:
    main()
except:
    main()
            

ser.close()
