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
GPIO.setup(22, GPIO.OUT, initial = GPIO.LOW)

p=GPIO.PWM(22, 1000)
p.start(1)
try:
    while 1:
        for dc in range(0, 51, 1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(50, -1, -1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)

except KeyboardInterrupt:
    print ("the program was  stoped by the keyboard")
    p.stop()
    
else:
    print("no expections")
finally:
    GPIO.output(dac, GPIO.LOW)
    
    print("GPIO cleanup completed")
GPIO.cleanup()
