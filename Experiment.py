# Let's run each sort and take the mean

from Selection_Sort import selection_sort
from Merge_Sort import merge_sort
import random
import time

# Performance testing
sizes_to_test = [500, 1000, 2000, 4000, 8000]

# Selection Sort
print("List of Selection Sort times:")
for n in sizes_to_test:
    times = []               # Creating an empty list to store the 5 running times
    for i in range(5):
        # Creating a random list containing n numbers
        test_list = [random.randint(1, 10000) for _ in range(n)]
        start = time.perf_counter()      # Starts the timer
        selection_sort(test_list)        # Runs the selection sort algorithm
        end = time.perf_counter()        # Stops the timer after sorting is done
        times.append(end - start)        # Calculates the difference between the starting and ending time and storing it
    mean_time = sum(times) / 5          # Calculates average running time

    print(f"n = {n}")                   # Print the input size and its average running time
    print(f"mean_time = {mean_time:.6f} seconds")
    print()

# Merge Sort
print("List of Merge Sort times:")
for n in sizes_to_test:
    times = []
    for i in range(5):
        test_list = [random.randint(1, 10000) for _ in range(n)]
        start = time.perf_counter()
        merge_sort(test_list)           # Runs the merge sort algorithm
        end = time.perf_counter()
        times.append(end - start)
    mean_time = sum(times) / 5

    print(f"n = {n}")                    # Print the input size and its average running time
    print(f"mean_time = {mean_time:.6f} seconds")
    print()


print("Selection Sort on already sorted lists:")
for n in sizes_to_test:
    test_list = list(range(n))
    start = time.perf_counter()
    selection_sort(test_list)      # Runs the selection sort on already sorted data
    end = time.perf_counter()
    print(f"n = {n}: {end - start:.6f} seconds")