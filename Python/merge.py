def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  
    right_half = merge_sort(arr[mid:])  

    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        sorted_array.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        sorted_array.append(right[right_index])
        right_index += 1

    return sorted_array
if __name__ == "__main__":
    array = [38, 27, 43, 3, 9, 82, 10]
    sorted_array = merge_sort(array)
    print("Sorted array:", sorted_array)
