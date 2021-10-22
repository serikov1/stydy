
# print('Hello, world!')
# x = 5
# name = 'Nikita'
# print('x is', x, 'name is', name, sep='\n', end='!')
# print(f'x is {x}, name is {name}')
# arr = [x, name, 42, '42', 'Something else']
# arr.append(6)
# print(arr)


x = [1, 2, 3, 4, 5]
y = []
for num in x:
    y.append(num * num)
coeffs = numpy.polyfit(x, y, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x]
pyplot.scatter(x, y, color='r')
pyplot.plot(x, line_points, color='b')
pyplot.xlabel('x, см')
pyplot.ylabel('y, с')
pyplot.xlim(0, 6)
pyplot.ylim(0, 30)
pyplot.grid()
pyplot.title('График зависимости иксов от их квадратов\nс линейной аппроксимацией')
pyplot.savefig('first')

<<<<<<< HEAD
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds =[21, 20, 16, 12, 7, 8, 25, 24]


def dec2bin(dec):
    binary = bin(dec) [2:]
    binary = binary [::-1]
    lw = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range (0, len(binary)):
        lw[i] = int(binary[i])
    lw.reverse()
    return lw

def number(dac, num):
    for n in range (0, 8):
        GPiO.output (dac[n], 0)
    for j in range (7, -1, -1):
        GPiO.output(dac[j], num[j])

def bin2dac(dac, K):
    L = dec2bin(K)
    number(dac, L)

def adc():
    n = 0
    m = 255
    i = int((n + m) / 2)
    while True:
        bin2dac(dac, i)
        bin2dac(leds, i)
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
    while adc() <255:
        GPiO.output(17, 0) #разрядили кондер
        print("000")
        time.sleep(0.1)

    start = time.time() #время начала 
    listT = [] #список времён
    listV = [] #список напряжений 
    measure = [] #список измеренных кодов напряжений 


    GPiO.output (17,1)
    while adc() < 252:
        listT.append(time.time() - start)
        measure.append(adc())
        listV.append((adc()*3.3)/256)
        time.sleep (0.1)
        print((adc()*3.3) / 256)
        print("111")
        if adc() >= 252:
            break 
        print(listT)

    GPiO.output(17, 0) 
    while adc() > 0:
        listT.append(time.time() - start)
        measure.append(adc())
        listV.append((adc()*3.3)/256)
        time.sleep (0.01)
        print("000")

    plt.plot(listV)
    plt.show()

    measure_str = [str(item for item  in measure)]

    with open('data.txt', 'w') as outfile:
        outfile.write("\n". join(measure_str))

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

    # plt.plot(listV)
    # # plt.title ('Зависимость напряжения на обкладках конденсатора от времени')
    # # plt.xlabel ('Время, с')   
    # # plt.ylabel ('Напряжение, В')
    # plt.show()

finally:
    GPiO.cleanup(leds)
    for i in range (7, -1, -1):
        GPiO.output(dac[i], 0) 
       
=======
>>>>>>> 1e4b3451be867166b7360c0802e21a1e2c05ec62
