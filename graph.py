
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

