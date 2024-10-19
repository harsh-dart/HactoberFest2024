# Define the array and target
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

# Initialize pointers
left = 0
right = len(array) - 1
found_index = -1  # To store the index if found

# Perform binary search
while left <= right:
    mid = left + (right - left) // 2
    if array[mid] == target:
        found_index = mid
        break
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

# Output the result
if found_index != -1:
    print("Element found at index:", found_index)
else:
    print("Element not found")
