# Function to partition the array
def partition(arr, low, high):
    pivot = arr[high]  # Pivot element
    i = low - 1  # Pointer for the smaller element

    for j in range(low, high):
        # If the current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    # Place the pivot element at the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Function to perform QuickSort
def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the partition index
        pi = partition(arr, low, high)

        # Recursively sort the elements on either side of the partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Test the quick sort function
arr = [10, 80, 30, 90, 40, 50, 70]
n = len(arr)
print("Original array:", arr)

quick_sort(arr, 0, n - 1)

print("Sorted array:", arr)
