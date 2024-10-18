#include <iostream>
using namespace std;

#define N 4

bool isSafe(int maze[N][N], int x, int y) {
    // Check if x, y is valid index and cell is not blocked
    return (x >= 0 && x < N && y >= 0 && y < N && maze[x][y] == 1);
}

bool solveMazeUtil(int maze[N][N], int x, int y, int sol[N][N]) {
    // Base case: when rat reaches the bottom-right corner
    if (x == N - 1 && y == N - 1 && maze[x][y] == 1) {
        sol[x][y] = 1;
        return true;
    }

    // Check if maze[x][y] is a valid move
    if (isSafe(maze, x, y)) {
        // Mark the current cell as part of the solution path
        sol[x][y] = 1;

        // Move forward in the x-direction (right)
        if (solveMazeUtil(maze, x + 1, y, sol)) 
            return true;

        // If moving in x-direction doesn't work, move down in y-direction
        if (solveMazeUtil(maze, x, y + 1, sol))
            return true;

        // If none of the above moves work, backtrack: unmark the current cell
        sol[x][y] = 0;
        return false;
    }
    return false;
}

void printSolution(int sol[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << sol[i][j] << " ";
        }
        cout << endl;
    }
}

bool solveMaze(int maze[N][N]) {
    int sol[N][N] = { { 0, 0, 0, 0 },
                      { 0, 0, 0, 0 },
                      { 0, 0, 0, 0 },
                      { 0, 0, 0, 0 } };

    // Start from the top-left corner (0, 0)
    if (!solveMazeUtil(maze, 0, 0, sol)) {
        cout << "No solution exists" << endl;
        return false;
    }

    printSolution(sol);
    return true;
}

int main() {
    int maze[N][N] = { { 1, 0, 0, 0 },
                       { 1, 1, 0, 1 },
                       { 0, 1, 0, 0 },
                       { 1, 1, 1, 1 } };

    solveMaze(maze);
    return 0;
}
