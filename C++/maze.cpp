# Define the maze size
N = 4

# A utility function to print the solution matrix
def printSolution(sol):
    for i in sol:
        print(i)

# A utility function to check if x, y is valid for N x N maze
def isSafe(maze, x, y):
    return x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1

# A recursive utility function to solve the maze problem
def solveMazeUtil(maze, x, y, sol):
    # Base case: if x, y is the bottom-right corner, return true
    if x == N - 1 and y == N - 1 and maze[x][y] == 1:
        sol[x][y] = 1
        return True

    # Check if maze[x][y] is valid
    if isSafe(maze, x, y):
        # Mark x, y as part of the solution path
        sol[x][y] = 1

        # Move forward in the x direction
        if solveMazeUtil(maze, x + 1, y, sol):
            return True

        # If moving in the x direction doesn't work, move down in the y direction
        if solveMazeUtil(maze, x, y + 1, sol):
            return True

        # If none of the above movements work, unmark x, y (backtrack)
        sol[x][y] = 0
        return False

    return False

# This function solves the maze problem using backtracking
def solveMaze(maze):
    sol = [[0 for _ in range(N)] for _ in range(N)]

    if not solveMazeUtil(maze, 0, 0, sol):
        print("No solution exists")
        return False

    printSolution(sol)
    return True

# Main function
if __name__ == "__main__":
    maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1]]

    solveMaze(maze)
