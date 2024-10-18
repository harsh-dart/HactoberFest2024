def findMaxSubCubeSum(matrix, M, N, O):
    # Initialize the maximum sum to the smallest possible integer
    max_sum = float('-inf')

    # Iterate over the first dimension of the 3D array
    for start in range(M):
        temp = [[0] * O for _ in range(N)]

        # Iterate over the end dimension of the first dimension
        for end in range(start, M):
            # Update the temporary array with the current slice
            for row in range(N):
                for col in range(O):
                    temp[row][col] += matrix[end][row][col]

            # Apply a modified Kadane's algorithm on the 2D temp array
            for row in range(N):
                # Initialize the current max for Kadane's algorithm
                current_max = [0] * O
                for col in range(row, N):
                    # Calculate sums for the current row from row to col
                    for depth in range(O):
                        current_max[depth] += temp[col][depth]

                    # Apply Kadane's algorithm on the current_max array
                    current_kadane_sum = 0
                    for value in current_max:
                        current_kadane_sum += value
                        if current_kadane_sum > max_sum:
                            max_sum = current_kadane_sum
                        # Reset current_kadane_sum if it drops below 0
                        if current_kadane_sum < 0:
                            current_kadane_sum = 0

    # Return the maximum sum
    return max_sum

