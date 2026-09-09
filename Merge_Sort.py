def merge_sort(arr):
    if len(arr) <= 1:      # We're checking if the array has 1 or 0 element
        return arr
    mid = len(arr) // 2    # If it's not sorted, we divide the length of the array in half
    left = merge_sort(arr[:mid])   # Merge sorts from the start to the mid
    right = merge_sort(arr[mid:])  # Merge sorts from the mid to the end
    return merge(left, right)

def merge(left, right):     # This function will be doing the sorting of the splitted array
    result = []
    i = j = 0
    while i < len(left) and j < len(right):  # We compare to pick the smaller value
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result



















