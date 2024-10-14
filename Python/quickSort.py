# quicksort.py

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Example usage, optional:
if __name__ == "__main__":
    sample_array = [3, 6, 8, 10, 1, 2, 1]
    print("Sorted array:", quick_sort(sample_array))
