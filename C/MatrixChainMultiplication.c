#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

void MatrixChainMultiplication(int p[], int n) {
    int m[n][n]; // Matrix to store minimum multiplications
    int s[n][n]; // Matrix to store split positions

    // Initialize m and s matrices
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            m[i][j] = 0;
            s[i][j] = 0;
        }
    }

    // Fill the m and s matrices
    for (int d = 1; d < n - 1; d++) { // d is the chain length
        for (int i = 1; i < n - d; i++) { // Starting matrix
            int j = i + d; // Ending matrix
            int min = INT_MAX; // Set minimum to a large value

            for (int k = i; k < j; k++) {
                int q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]; // Cost of multiplication
                if (q < min) {
                    min = q; // Update minimum
                    s[i][j] = k; // Store split position
                }
            }
            m[i][j] = min; // Store minimum multiplications
        }
    }

    // Display the m matrix
    printf("M matrix:\n");
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < n; j++) {
            printf("%d ", m[i][j]);
        }
        printf("\n");
    }

    // Display the s matrix
    printf("S matrix (split positions):\n");
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < n; j++) {
            printf("%d ", s[i][j]);
        }
        printf("\n");
    }

    printf("\nMinimum number of multiplications is: %d\n", m[1][n - 1]);
}

int main() {
    int n;
    printf("Enter the number of matrices you want to multiply: ");
    scanf("%d", &n);

    int d[n + 1];
    printf("Enter dimensions for each matrix (d1, d2, ..., dn):\n");
    for (int i = 0; i < n + 1; i++) {
        printf("Enter dimension #%d: ", i + 1);
        scanf("%d", &d[i]);
    }

    MatrixChainMultiplication(d, n + 1);

    return 0;
}
