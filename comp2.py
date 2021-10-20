import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
troykaModule = 17
comparator = 4

def decimal2binary(value):
    return [int (element) for element in bin(value)[2:].zfill(bits)]

def bin2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    return signal


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troykaModule, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comparator, GPIO.IN)
try:
    while True:
        a=0
        b=255
        value = int((a+b)/2)
        while True:
            signal = bin2dac(value)
            voltage = value / levels * maxVoltage
            time.sleep(0.007)
            if b - a == 2:
                comparatorValue = GPIO.input(comparator)
                print ("ADC value = {:^3} -> {}, input voltag = {:.2f}". format(value, signal, voltage))
                break
            elif GPIO.input(comparator)  == 1:
                a = value
                value = int((a+b)/2)
            elif GPIO.input(comparator)  == 0:
                b = value
                value = int((a+b)/2)   
        
        
except KeyboardInterrupt:
    print ("the program was  stoped by the keyboard")
else:
    print("no expections")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print("GPIO cleanup completed")