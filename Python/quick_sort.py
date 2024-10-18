# Function to perform the partition
def partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as the pivot
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot element with element at i+1
    return i + 1

# Function to perform QuickSort
def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)

        # Recursively sort elements before and after the partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Get input from the user
arr = list(map(int, input("Enter numbers separated by space: ").split()))
n = len(arr)

print("Original array:", arr)
quick_sort(arr, 0, n - 1)
print("Sorted array:", arr)
