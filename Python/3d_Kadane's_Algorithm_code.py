def findMaxSubCubeSum(matrix, M, N, O):
    # Initialize the maximum sum to the smallest possible integer
    maxSum = -(1 << 60)

    # Iterate over the first dimension of the 3D array
    for i in range(M):
        # Initialize a 2D temporary array to store intermediate sums
        temp = [[0] * N for _ in range(N)]

        # Iterate over the first dimension again
        for j in range(i, M):
            # Iterate over the second and third dimensions
            for k in range(N):
                for l in range(O):
                    # Add the current element to the temporary array
                    temp[k][l] += matrix[j][k][l]

            # Iterate over the second dimension
            for k in range(N):
                # Initialize another temporary array to store intermediate sums
                innerTemp = [0] * O
                kadane2 = [0] * O

                # Iterate over the second dimension again
                for l in range(k, N):
                    # Iterate over the third dimension
                    for m in range(O):
                        # Add the current element to the inner temporary array
                        innerTemp[m] += temp[l][m]

                    # Copy the inner temporary array to another array
                    kadane2 = innerTemp[:]

                    for m in range(O):
                        # If not the first element, add the previous element to the current element
                        if m > 0:
                            kadane2[m] += kadane2[m - 1]
                        # If the current element is greater than the maximum sum, update the maximum sum
                        if kadane2[m] > maxSum:
                            maxSum = kadane2[m]
                        # If the current element is less than 0, set it to 0
                        if kadane2[m] < 0:
                            kadane2[m] = 0

    # Return the maximum sum
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
# This code is contributed by Rupesh Kumar(kumarrupesh2310)
