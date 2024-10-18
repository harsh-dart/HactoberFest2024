import time
import random

# Merge function that merges two halves in the chosen order (ascending or descending)
def merge(arr, left, mid, right, ascending=True):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temporary arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    # Merge the temp arrays back into arr[left..right]
    while i < n1 and j < n2:
        if (L[i] <= R[j] and ascending) or (L[i] >= R[j] and not ascending):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    # Visualization of the current step
    print(f"Current list: {arr}")

# Merge sort function
def mergeSort(arr, left, right, ascending=True):
    if left < right:
        mid = (left + right) // 2

        # Sort first and second halves
        mergeSort(arr, left, mid, ascending)
        mergeSort(arr, mid + 1, right, ascending)

        # Merge the sorted halves
        merge(arr, left, mid, right, ascending)

# Function to let the user choose manual input or random list generation
def input_choice():
    choice = input("Enter 'M' for manual input or 'R' for random input: ").lower()
    if choice == 'm':
        size = int(input("Enter the size of the list: "))
        arr = []
        print("Enter the elements of the list:")
        for i in range(size):
            element = int(input(f"Element {i + 1}: "))
            arr.append(element)
    else:
        size = int(input("Enter the size of the random list: "))
        arr = random.sample(range(1, 100), size)  # Generate a random list
        print(f"Random list generated: {arr}")
    return arr

# Function to choose sorting order
def order_choice():
    order = input("Enter 'A' for ascending order or 'D' for descending order: ").lower()
    return order == 'a'

def run_merge_sort():
    arr = input_choice()
    ascending = order_choice()

    print("Initial list:", arr)
    
    # Calculate execution time
    start_time = time.time()
    mergeSort(arr, 0, len(arr) - 1, ascending)
    end_time = time.time()

    print("Sorted list:", arr)
    print(f"Execution time: {end_time - start_time:.6f} seconds")

# Main function
if __name__ == "__main__":
    run_merge_sort()

