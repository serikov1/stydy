# import matplotlib.pyplot as plt
m = [10, 20, 30, 40, 50 ,60, 88]
plt.plot(m)
plt.show()

m_str = [str(item) for item in m]

with open('data.txt', 'w') as file:
    file.write(m_str)