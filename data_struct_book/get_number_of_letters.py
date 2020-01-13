import matplotlib.pyplot as plt

def read_file(filename):
    file = open("test.txt", 'r')

    pocet_pismen = {}

    for line in file:
        for letter in line:
            if letter.lower() in pocet_pismen:
                pocet_pismen[letter.lower()] += 1
            else:
                pocet_pismen[letter.lower()] = 1


    file.close()
    return pocet_pismen

pocet_pismen = read_file('test.txt')

pocet_pismen = dict(sorted(pocet_pismen.items(), key=lambda x: x[1], reverse=True))

x = []
y = []
for i in pocet_pismen.keys():
    x.append(i)

for i in pocet_pismen.values():
    y.append(i)

y_ticks = []
for i in range(0, y[0]+5, 20):
    y_ticks.append(i)

plt.bar(x, y)
plt.yticks(y_ticks)
plt.show()