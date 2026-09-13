import matplotlib.pyplot as plt
import numpy as np

x = np.array([2021, 2022, 2023, 2024])
y1 = np.array([15, 20, 1000, 30])
y2 = np.array([12, 28, 45, 63])
y3 = np.array([1, 85, 36, 27])

line_style = dict(marker=".",
                  markersize=20,
                  markerfacecolor="red",
                  markeredgecolor="red",
                  linestyle="solid",
                  linewidth=2)
plt.title("Class size", fontsize=25,
                             family="Times New Roman",
                             fontweight="bold",
                             color="black")

plt.xlabel("Year", fontsize=20,
                          family="Times New Roman",
                          fontweight="bold",
                          color="black")

plt.ylabel("Students", fontsize=20,
                              family="Times New Roman",
                              fontweight="bold",
                              color="black")

plt.tick_params(axis='both',
                which='major',
                labelsize=20)

plt.plot(x, y1, color='#d93d3f', **line_style)
plt.plot(x, y2, color='#2765e3', **line_style)
plt.plot(x, y3, color='#27e33a', **line_style)

plt.xticks(x)

plt.show()



