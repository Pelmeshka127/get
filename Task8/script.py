import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

with open("settings.txt", "r") as file:
    settings = [float(i) for i in file.read().split("\n")]

data = np.loadtxt("data.txt", dtype = int) * settings[1]

data_time = np.array([i * settings[0] for i in range(data.size)])


fig, ax = plt.subplots(figsize = (8, 6), dpi = 100)

plt.title("Процесс заряда и разряда конденстаора в RC-цепочке")

plt.ylabel("$y = Напряжение$, $В$")
plt.xlabel("$x = Время$, $c$")

ax.axis([data.min(), data_time.max()+1, data.min(), data.max()+0.2])

ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))

ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

ax.grid(which = "major", color = "b")
ax.minorticks_on()
ax.grid(which = "minor", color = "blue", linestyle = ":")

plt.plot(data_time, data, c="black", linewidth = 1, label = "V(t)")
plt.text(50,2.2, "Время зарядки = 36с")
plt.text(50,2.0, "Время разрядки = 72с")

ax.legend(shadow = False, loc = "right", fontsize = 30)
ax.scatter(data_time[0:data.size:200], data[0:data.size:200], marker = "s", c = "blue", s = 50)

fig.savefig("grap.svg")
fig.savefig("grap.png")

plt.show()