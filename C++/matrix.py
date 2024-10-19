def binary_search_in_matrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    left = 0
    right = rows * cols - 1  # Treat the 2D matrix as a 1D array

    while left <= right:
        mid = left + (right - left) // 2  # Find the middle index
        mid_value = matrix[mid // cols][mid % cols]  # Map the mid index to 2D matrix

        if mid_value == target:
            print(f"Element found at ({mid // cols}, {mid % cols})")
            return True
        elif mid_value < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    print("Element not found.")
    return False

def main():
    # Example sorted matrix (3x4)
    matrix = [
        [1, 4, 7, 11],
        [2, 5, 8, 12],
        [3, 6, 9, 16]
    ]

    target = 5  # Element to search for

    binary_search_in_matrix(matrix, target)  # Function call

if __name__ == "__main__":
    main()

