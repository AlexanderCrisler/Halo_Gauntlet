import serial
import time
ser = serial.Serial('COM3', 9600)

while True:
    select = input('1-5: ')
    if select >= 1 and select <= 5:
        ser.write(select)
    else:
        print('incorrect input.')

ser.close()