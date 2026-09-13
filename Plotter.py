import matplotlib.pyplot as plt
import numpy as np

input_size = np.array([500, 1000, 2000, 4000, 8000])
selection_random_times = np.array([0.007762, 0.028622, 0.131519, 0.332820, 1.050621])
merge_random_times = np.array([0.000599, 0.001508, 0.003153, 0.006862, 0.013503])
selection_sorted_times = np.array([0.003874, 0.014754, 0.085671, 0.281876, 1.051211])

line_style = dict(marker=".",
                  markersize=20,
                  linestyle="solid",
                  linewidth=2)

plt.title("Sorting Algorithm Performance", fontsize=25,
                                                family="Times New Roman",
                                                fontweight="bold",
                                                color="black")

plt.xlabel("Input Size (n)", fontsize=16,
                                    family="Times New Roman",
                                    fontweight="bold",
                                    color="black")

plt.ylabel("Time (sec)", fontsize=16,
                                family="Times New Roman",
                                fontweight="bold",
                                color="black")

plt.plot(input_size,
         selection_random_times,
         color='#d93d3f',
         markerfacecolor='#d93d3f',
         markeredgecolor='#d93d3f',
         label="Selection sort(Random Input)",
         **line_style)

plt.plot(input_size,
         merge_random_times,
         color='#2765e3',
         markerfacecolor='#2765e3',
         markeredgecolor='#2765e3',
         label="Merge sort(Random Input)",
         **line_style)

plt.plot(input_size,
         selection_sorted_times,
         color='#27e33a',
         markerfacecolor='#27e33a',
         markeredgecolor='#27e33a',
         label="Selection sort(Sorted Input)",
         **line_style)

plt.legend(loc="upper left")
plt.grid(True)
plt.xticks(input_size)

plt.show()