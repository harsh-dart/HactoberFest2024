# Quick Sort Algorithm

def quick_sort(arr):
    # Base case: If the array has 0 or 1 element, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Recursive case: Partitioning the array and sorting the subarrays
    pivot = arr[len(arr) // 2]  # Choose pivot as middle element
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    # Recursively apply quick_sort to the left and right parts
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
if __name__ == "__main__":
    # Input list
    arr = [12, 4, 5, 6, 7, 3, 1, 15]
    
    print("Original array:", arr)
    
    # Sorting the array
    sorted_arr = quick_sort(arr)
    
    print("Sorted array:", sorted_arr)
