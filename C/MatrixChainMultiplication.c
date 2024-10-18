#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

void MatrixChainMultiplication(int p[], int n) {
    // Initialize matrices m and s
    int m[n][n];
    int s[n][n];

    // Setting the diagonal to 0 since cost of multiplying one matrix is zero
    for (int i = 1; i < n; i++) {
        m[i][i] = 0; // Cost of multiplying one matrix is zero
    }

    // Calculate minimum multiplications
    for (int d = 1; d < n; d++) {  // The number of matrices to be multiplied
        for (int i = 1; i < n - d; i++) { // Starting matrix
            int j = i + d; // Ending Matrix
            m[i][j] = INT_MAX; // Set to maximum value to find the minimum
            for (int k = i; k < j; k++) {
                int q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]; // Formula for MCM
                if (q < m[i][j]) { // Comparing the number of multiplications
                    m[i][j] = q; // Assigning the minimum multiplications
                    s[i][j] = k; // Storing the split position
                }
            }
        }
    }

    // Display the M matrix
    printf("M matrix:\n");
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < n; j++) {
            printf("%d ", m[i][j]);
        }
        printf("\n");
    }

    // Display the S matrix
    printf("S matrix (split positions):\n");
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < n; j++) {
            printf("%d ", s[i][j]);
        }
        printf("\n");
    }

    printf("\nMinimum number of multiplications is: %d\n\n", m[1][n - 1]);
}

int main() {
    int n;
    printf("Enter the number of matrices you want to multiply: ");
    scanf("%d", &n);

    int *d = (int *)malloc((n + 1) * sizeof(int)); // Allocate memory for dimensions
    printf("Enter dimensions for each matrix (d1, d2, ..., dn):\n");
    for (int i = 0; i < n + 1; i++) {
        printf("Enter dimension #%d: ", i + 1);
        scanf("%d", &d[i]);
    }

    MatrixChainMultiplication(d, n + 1);

    free(d); // Free the allocated memory for dimensions
    return 0;
}
