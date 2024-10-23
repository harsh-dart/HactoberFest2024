def binary_search(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Indicates that the target was not found

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search(array, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
