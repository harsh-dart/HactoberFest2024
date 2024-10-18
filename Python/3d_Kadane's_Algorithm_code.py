def findMaxSubCubeSum(matrix, M, N, O):
    # Initialize the maximum sum to a very small value
    maxSum = -(1 << 60)

    # Iterate over the first dimension of the 3D matrix
    for i in range(M):
        # Initialize a 2D temporary array for storing intermediate sums
        temp = [[0] * O for _ in range(N)]

        # Iterate over the first dimension again for sub-cube boundaries
        for j in range(i, M):
            # Update the temporary array with the sum of elements between i and j
            for k in range(N):
                for l in range(O):
                    temp[k][l] += matrix[j][k][l]

            # Iterate over possible submatrices in the 2D plane (N x O)
            for k in range(N):
                # Array to store sums for Kadane's algorithm across the 3rd dimension
                innerTemp = [0] * O
                kadane2 = [0] * O

                # Iterate over rows in the current submatrix
                for l in range(k, N):
                    for m in range(O):
                        innerTemp[m] += temp[l][m]

                    # Apply Kadane's algorithm to find the maximum subarray sum
                    kadane2 = innerTemp[:]
                    for m in range(O):
                        if m > 0:
                            kadane2[m] += kadane2[m - 1]

                        if kadane2[m] > maxSum:
                            maxSum = kadane2[m]
                        
                        if kadane2[m] < 0:
                            kadane2[m] = 0

    # Return the maximum sum found in the sub-cube
    return maxSum


# Example inputs
M = 3
N = 3
O = 3
matrix = [
    [[-1, -2, 3], [-4, -5, 6], [7, 8, 9]],
    [[-9, -8, 7], [-6, -5, 4], [3, 2, 1]],
    [[-1, -3, 5], [-7, -9, 2], [4, 6, 8]]
]

# Call the function to find the maximum sum of a sub-cube in the 3D array
result = findMaxSubCubeSum(matrix, M, N, O)

# Output the result
print("The maximum sum of a sub-cube in the 3D array is:", result)
