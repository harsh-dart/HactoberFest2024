def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Find the middle index
        if nums[mid] == target:
            return mid  # Return the index if the target is found
        elif nums[mid] < target:
            left = mid + 1  # Search the right half
        else:
            right = mid - 1  # Search the left half
    
    return -1  # Return -1 if the target is not found

if __name__ == "__main__":
    # Sample input (sorted array)
    nums = [2, 7, 11, 15]
    target = 11

    # Call the binary_search function
    result = binary_search(nums, target)

    # Output the result
    if result != -1:
        print(f"Target found at index: {result}")
    else:
        print("Target not found in the array.")
