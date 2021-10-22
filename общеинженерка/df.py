import RPi.GPIO as GPiO

# import matplotlib.pyplot as plt
import numpy as np 


import time





GPiO.setmode(GPiO.BCM)
GPiO.setup(26, GPiO.OUT)
GPiO.setup(19, GPiO.OUT)
GPiO.setup(13, GPiO.OUT)
GPiO.setup(6, GPiO.OUT)
GPiO.setup(5, GPiO.OUT)
GPiO.setup(11, GPiO.OUT)
GPiO.setup(9, GPiO.OUT)
GPiO.setup(10, GPiO.OUT)
GPiO.setup(4, GPiO.IN)
GPiO.setup(17, GPiO.OUT)

P=[26,19,13,6,5,11,9,10]

GPiO.setmode(GPiO.BCM)
GPiO.setup(21, GPiO.OUT)
GPiO.setup(20, GPiO.OUT)
GPiO.setup(16, GPiO.OUT)
GPiO.setup(12, GPiO.OUT)
GPiO.setup(7, GPiO.OUT)
GPiO.setup(8, GPiO.OUT)
GPiO.setup(25, GPiO.OUT)
GPiO.setup(24, GPiO.OUT)
GPiO.setup(4, GPiO.IN)
GPiO.setup(17, GPiO.OUT)

P1=[21,20,16,12,7,8,25,24]


def dec2bin(dec):
    binary = bin(dec) [2:]
    binary = binary [::-1]
    lw = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range (0, len(binary)):
        lw[i] = int(binary[i])
    lw.reverse()
    return lw

def logicnumber(P, num):
    for n in range (0, 8):
        GPiO.output (P[n], 0)
    for j in range (7, -1, -1):
        GPiO.output(P[j], num[j])

def bin2dac(P, K):
    L = dec2bin(K)
    logicnumber(P, L)

def adc():
    n = 0
    m = 255
    i = int((n + m) / 2)
    while True:
        bin2dac(P, i)
        bin2dac(P1, i)
        time.sleep(0.01)
        if m - n == 2 or i == 0:
            Volt =  (((i* 3.3) / 256))
            print("Digital value: ", i, ", Analog Value: ", Volt, "V")
            return i 
            break
        elif GPiO.input(4) == 1:
            n = i
            i = int ((n+m) / 2)
        elif GPiO.input(4) == 0:
            m = i
            i = int((n+m) / 2)
try:
    while adc() > 0:
        GPiO.output(17, 0) #разрядили кондер
        print("000")
        time.sleep(1)

    start = time.time() #время начала 
    listT = [] #список времён
    listV = [] #список напряжений 
    measure = [] #список измеренных кодов напряжений 

    GPiO.output (17,1) #заряжаем кондёр
    while adc() < 252:
        listT.append(time.time() - start)
        measure.append(adc())
        listV.append((adc()*3.3)/256)
        time.sleep(0.01)
        print((adc()*3.3) / 256)
        print("111")
        if adc() >= 252:
            break 

    GPiO.output(17, 0) #заряжаем кондёр
    while adc() > 0:
        listT.append(time.time() - start)
        measure.append(adc())
        listV.append((adc()*3.3)/256)
        time.sleep (0.01)
        print("000")

    plt.plot(measure, 'r-')
    plt.show()

    np.savetxt('data.txt', measure, fmt='%f')

    dT = 0
    for i in range (0, len(listT)-1):
        dT = dT + abs(listV[i+1] - listV[i])
        dT = dT / (len(listT) - 1)
        dV = 0
    for i in range (0, len(listT)-1):
        dV = dV + abs(listV[i+1] - listV[i])
    dV = dV / (len(listT) - 1)
    x = [dT, dV]
    np.savetxt('settings.txt', x, fmt='%f')

    plt.plot(listT, listV, 'r-')
    plt.title ('Зависимость напр на обкладках кондёра от времени')
    plt.xlabel ('Время, с')   
    plt.ylabel ('Напряжение, В')
    plt.show()

finally:
    for i in range (7, -1, -1):
        GPiO.output(P[i], 0)