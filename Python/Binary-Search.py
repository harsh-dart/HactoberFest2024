def binary_search(array, target):
    left = 0
    right = len(array) - 1
    found_index = -1  # Initialize found_index to -1, indicating not found

    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index
        if array[mid] == target:
            found_index = mid  # Store the index where the target is found
            break  # Target found, exit the loop
        elif array[mid] < target:
            left = mid + 1  # Narrow down to the right half
        else:
            right = mid - 1  # Narrow down to the left half

    # Output the result based on found_index
    if found_index != -1:
        print("Element found at index:", found_index)
    else:
        print("Element not found")

# Example usage
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
binary_search(array, target)
