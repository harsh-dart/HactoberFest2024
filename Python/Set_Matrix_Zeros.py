from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Step 1: Handle edge case for an empty matrix
        if not matrix:
            return
        
        rows, cols = len(matrix), len(matrix[0])
        # Step 2: Use the first row and first column as markers
        row_zero = any(matrix[0][col] == 0 for col in range(cols))
        col_zero = any(matrix[row][0] == 0 for row in range(rows))
        
        # Step 3: Mark zeros in the first row and first column
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        
        # Step 4: Set the elements to zero based on markers
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        # Step 5: Handle the first row and first column
        if row_zero:
            for col in range(cols):
                matrix[0][col] = 0
        if col_zero:
            for row in range(rows):
                matrix[row][0] = 0

# Test cases
def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()

# Example 1
matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print("Input:")
print_matrix(matrix1)
Solution().setZeroes(matrix1)
print("Output:")
print_matrix(matrix1)

# Example 2
matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print("Input:")
print_matrix(matrix2)
Solution().setZeroes(matrix2)
print("Output:")
print_matrix(matrix2)
