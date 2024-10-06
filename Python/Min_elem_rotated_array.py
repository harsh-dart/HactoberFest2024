def find_min_in_rotated_array(arr):
    low = 0
    high = len(arr) - 1
    
    if arr[low] <= arr[high]:
        return arr[low]

    while low <= high:
        mid = (low + high) // 2
        
        if mid > 0 and arr[mid] < arr[mid - 1]:
            return arr[mid]
        
        if mid < len(arr) - 1 and arr[mid] > arr[mid + 1]:
            return arr[mid + 1]
        
        if arr[mid] >= arr[low]:
            low = mid + 1
        else:
            high = mid - 1

    return -1

rotated_array = [4, 5, 6, 7, 0, 1, 2]
min_element = find_min_in_rotated_array(rotated_array)
print("The minimum element is:", min_element)
