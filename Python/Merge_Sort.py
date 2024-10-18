import time
import random

def merge_sort(arr, ascending=True, visualize=False):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid], ascending, visualize)
    right_half = merge_sort(arr[mid:], ascending, visualize)
    
    merged = merge(left_half, right_half, ascending)
    
    if visualize:
        print(f"Merging: {left_half} + {right_half} => {merged}")
    
    return merged

def merge(left, right, ascending):
    sorted_list = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if (ascending and left[i] <= right[j]) or (not ascending and left[i] >= right[j]):
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    
    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    
    return sorted_list

def get_user_input():
    while True:
        try:
            n = int(input("Enter the number of elements in the array: "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            return n
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_array_elements(n):
    arr = []
    print(f"Enter {n} integers:")
    for _ in range(n):
        while True:
            try:
                arr.append(int(input()))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
    return arr

def generate_random_array(n):
    return [random.randint(-10**9, 10**9) for _ in range(n)]

def main():
    print("Welcome to the Enhanced Merge Sort Program!")
    
    # User can choose between manual input or random array generation
    option = input("Do you want to input the array manually (M) or generate a random array (R)? ").lower()
    
    if option == 'm':
        n = get_user_input()
        arr = get_array_elements(n)
    elif option == 'r':
        n = get_user_input()
        arr = generate_random_array(n)
        print(f"Generated Random Array: {arr}")
    else:
        print("Invalid choice. Please restart the program.")
        return
    
    # User can choose the sorting order
    order = input("Do you want to sort in Ascending (A) or Descending (D) order? ").lower()
    ascending = order == 'a'
    
    # Option to visualize the merging process
    visualize = input("Would you like to visualize the merging process (Y/N)? ").lower() == 'y'
    
    # Start timing the sorting process
    start_time = time.time()
    
    # Perform merge sort
    sorted_arr = merge_sort(arr, ascending, visualize)
    
    # End timing
    end_time = time.time()
    
    # Display the result
    print(f"\nSorted array: {sorted_arr}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    main()
