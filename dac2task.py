import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3

def decimal2binary(value):
    return [int (element) for element in bin(value)[2:].zfill(bits)]

def bin2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    return signal


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

try:
    for i in range(256):
        bin2dac(i)
        time.sleep(0.01)
    for i in range(255, -1, -1):
        bin2dac(i)
        time.sleep(0.01)


except KeyboardInterrupt:
    print ("the program was  stoped by the keyboard")
else:
    print("no expections")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print("GPIO cleanup completed")