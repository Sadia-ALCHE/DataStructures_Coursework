import matplotlib.pyplot as plt
import numpy as np

x = np.array([2021, 2022, 2023, 2024])
y = np.array([15, 20, 1000, 30])

plt.plot(x, y, marker=".",
                     markersize=20,
                     markerfacecolor="red",
                     markeredgecolor="red",
                     linestyle="solid",
                     linewidth=2,
                     color="#d93d3f")
plt.show()



# Plot all three curves on one chart
# plt.figure(figsize=(10, 6))
#
# plt.plot(
#     sizes,
#     selection_random_times,
#     marker="o",
#     label="Selection Sort - Random Input"
# )
#
# plt.plot(
#     sizes,
#     merge_random_times,
#     marker="o",
#     label="Merge Sort - Random Input"
# )
#
# plt.plot(
#     sizes,
#     selection_sorted_times,
#     marker="o",
#     label="Selection Sort - Already Sorted Input"
# )
#
# plt.xlabel("Input size (n)")
# plt.ylabel("Time (seconds)")
# plt.title("Sorting Algorithm Performance")
# plt.legend()
# plt.grid(True)
#
# plt.show()