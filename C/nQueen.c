#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Function to print the solution board
void printSolution(int N, int **board) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++)
            printf("%2d ", board[i][j]);
        printf("\n");
    }
}

// Function to check if a queen can be placed safely
bool isSafe(int N, int **board, int row, int col) {
    // Check this row on the left side
    for (int i = 0; i < col; i++)
        if (board[row][i])
            return false;

    // Check upper diagonal on the left side
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j])
            return false;

    // Check lower diagonal on the left side
    for (int i = row, j = col; i < N && j >= 0; i++, j--)
        if (board[i][j])
            return false;

    return true;
}

// Recursive utility function to solve the N-Queens problem
bool solveNQueensUtil(int N, int **board, int col) {
    if (col >= N)
        return true;

    for (int i = 0; i < N; i++) {
        if (isSafe(N, board, i, col)) {
            board[i][col] = 1; // Place queen

            if (solveNQueensUtil(N, board, col + 1)) // Recur
                return true;

            board[i][col] = 0; // Backtrack
        }
    }

    return false; // No place for a queen in this column
}

// Main function to solve the N-Queens problem
bool solveNQueens(int N) {
    // Dynamically allocate memory for the board
    int **board = (int **)malloc(N * sizeof(int *));
    for (int i = 0; i < N; i++) {
        board[i] = (int *)malloc(N * sizeof(int));
    }

    // Initialize the board to 0
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            board[i][j] = 0;

    if (!solveNQueensUtil(N, board, 0)) {
        printf("Solution does not exist.\n");
        // Free allocated memory
        for (int i = 0; i < N; i++) {
            free(board[i]);
        }
        free(board);
        return false;
    }

    printf("Solution for %d-Queens problem:\n", N);
    printSolution(N, board);

    // Free allocated memory
    for (int i = 0; i < N; i++) {
        free(board[i]);
    }
    free(board);
    return true;
}

int main() {
    int N;

    printf("Enter the value of N: ");
    scanf("%d", &N);

    solveNQueens(N);

    return 0;
}
