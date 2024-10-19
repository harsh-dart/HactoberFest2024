def merge_sort(array):
    if len(array) > 1:
        # Find the midpoint of the array
        mid_point = len(array) // 2
        
        # Split the array into two halves
        left_half = array[:mid_point]
        right_half = array[mid_point:]
        
        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Merge the sorted halves
        merge(array, left_half, right_half)

def merge(array, left_half, right_half):
    i = j = k = 0
    
    # Merging the sorted halves
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:  # Changed to <= for stable sort
            array[k] = left_half[i]
            i += 1
        else:
            array[k] = right_half[j]
            j += 1
        k += 1
    
    # Copy remaining elements of left_half if any
    while i < len(left_half):
        array[k] = left_half[i]
        i += 1
        k += 1
    
    # Copy remaining elements of right_half if any
    while j < len(right_half):
        array[k] = right_half[j]
        j += 1
        k += 1

# Example usage:
if __name__ == "__main__":
    sample_array = [12, 11, 13, 5, 6, 7]
    print("Given array is:", sample_array)
    merge_sort(sample_array)
    print("Sorted array is:", sample_array)
