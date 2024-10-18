def quick_sort(arr):
    """Quick Sort algorithm to sort an array."""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choosing the middle element as pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


# Example usage:
if __name__ == "__main__":
    sample_data = [33, 10, 59, 26, 2, 89, 4, 0, 19]
    print("Unsorted Array:", sample_data)
    sorted_data = quick_sort(sample_data)
    print("Sorted Array:", sorted_data)
