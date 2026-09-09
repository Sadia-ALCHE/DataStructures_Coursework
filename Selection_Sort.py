# Selection_Sort.py
# Ths file contains the sorting algorithms that will be used throughout this assignment

def selection_sort(arr):
    for i in range(len(arr)): #To find the length of the list
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]: #If the next number is smaller than the current index,
                min_index = j           # that becomes our new minimum index
        arr[i], arr[min_index] = arr[min_index], arr[i]  #Once the smallest number is found, they swap
    return arr
















