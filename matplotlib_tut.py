from matplotlib import pyplot as plt

'''dev_x = [25,26,27,28,29,30,31,32,33,34,35]
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(dev_x, dev_y)

plt.xlabel('Věk')
plt.ylabel('Plat')
plt.title("Plat programátorů (CZE) podle věku")
'''
plt.style.use('ggplot')
x_values = []
y_values = []

for x in range(-8, 5):
    x_values.append(x)
    y_values.append(abs(2 - abs(x + 3)))

plt.plot(x_values, y_values, linewidth=3)

y_values = []
for x in range(-8, 5):
    y_values.append(2 - abs(x + 3))

plt.plot(x_values, y_values, linestyle=':', linewidth=3)

plt.xlabel('X')
plt.ylabel('Y')
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.legend(['|2-|x+3||', '2-|x+3|'])
plt.grid(True)

'''plt.xlim(left=-8, right=3)
plt.ylim(bottom=-5, top=5)'''

plt.show()