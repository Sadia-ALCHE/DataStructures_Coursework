def merge_sort(arr):
    if len(arr) <= 1:      # An array with 0 or 1 element is already sorted
        return arr
    mid = len(arr) // 2    # If it's not sorted, we divide the length of the array in half
    left = merge_sort(arr[:mid])   # Merge sorts from the start to the mid
    right = merge_sort(arr[mid:])  # Merge sorts from the mid to the end
    return merge(left, right)      # Merge the two sorted halves

def merge(left, right):     # Combines two sorted arrays into one sorted array
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])       # This adds any remaining elements from the left
    result.extend(right[j:])      # This adds any remaining elements from the right
    return result



















