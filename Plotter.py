import matplotlib.pyplot as plt
import numpy as np

input_size = np.array([500, 1000, 2000, 4000, 8000])
selection_sort_random = np.array([0.007762, 0.028622, 0.131519, 0.332820, 1.050621])
merge_sort_random = np.array([0.000599, 0.001508, 0.003153, 0.006862, 0.013503])
selection_sort_sorted = np.array([0.003874, 0.014754, 0.085671, 0.281876, 1.051211])

line_style = dict(marker=".",
                  markersize=20,
                  linestyle="solid",
                  linewidth=2)

plt.plot(input_size,
         selection_sort_random,
         label="Selection sort")