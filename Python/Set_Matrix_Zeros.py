from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Step 1: Handle edge case for an empty matrix
        if not matrix or not matrix[0]:
            return
        
        rows, cols = len(matrix), len(matrix[0])
        
        # Step 2: Use the first row and first column as markers
        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))
        
        # Step 3: Mark zeros in the first row and first column
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Step 4: Set the cells to zero based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Step 5: Set the first row and first column to zero if needed
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0

# Test cases
def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()

# Example 1
matrix1 = [[1,1,1], [1,0,1], [1,1,1]]
print("Input:")
print_matrix(matrix1)

Solution().setZeroes(matrix1)
print("Output:")
print_matrix(matrix1)

# Example 2
matrix2 = [[0,1,2,0], [3,4,5,2], [1,3,1,5]]
print("Input:")
print_matrix(matrix2)

Solution().setZeroes(matrix2)
print("Output:")
print_matrix(matrix2)
