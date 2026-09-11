# Let's test it now

from Selection_Sort import selection_sort
from Merge_Sort import merge_sort

test_case = {
    'sorted' : [1, 2, 3, 4, 5],
    'unsorted' : [5, 4, 1, 3, 2],
    'with_repeated_values' : [2, 4, 6, 1, 2, 3, 5, 4]
}

print('Testing Selection Sort:')                  # Let's test for selection sort
for name, test_list in test_case.items():
    result = selection_sort(test_list.copy())
    print(name, ":", result)

print('\nTesting Merge Sort:')                   # Let's test for merge sort
for name, test_list in test_case.items():
    result = merge_sort(test_list.copy())
    print(name, ":", result)
