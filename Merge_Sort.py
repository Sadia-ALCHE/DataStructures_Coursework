def merge_sort(arr):
    if len(arr) <= 1:      # We're checking if the array has 1 or 0 element
        return arr
    mid = len(arr) // 2    # If it's not sorted, we divide the length of the array in half
    left = merge_sort(arr[:mid])   #Merge sorts from the start to the mid
    right = merge_sort(arr[mid:]) # Merge sorts from the mid to the end
    return merge_sort(left) + [right]


















