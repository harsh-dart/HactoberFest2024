def solveNQueens(N: int):
    def is_safe(board, row, col):
        # Check this column on upper side
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        # Check upper diagonal on right side
        for i, j in zip(range(row, -1, -1), range(col, N)):
            if board[i][j] == 'Q':
                return False

        return True

    def solve(board, row):
        if row == N:
            # Store the configuration
            solution = ["".join(row) for row in board]
            solutions.append(solution)
            return

        for col in range(N):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                solve(board, row + 1)
                board[row][col] = '.'

    # Initialize the chessboard
    board = [['.' for _ in range(N)] for _ in range(N)]
    solutions = []
    solve(board, 0)
    return solutions


def print_solution(solution):
    board_size = len(solution)
    print("\n" + "=" * (2 * board_size - 1))
    for row in solution:
        print(" | ".join(row))
        print("-" * (2 * board_size - 1))
    print("=" * (2 * board_size - 1) + "\n")


def main():
    # Get N value from the user
    try:
        N = int(input("Enter the value of N (between 1 and 10): "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    # Validate the input
    if N <= 0 or N > 10:
        print("Enter N value from 1 to 10.")
        return

    # Solve N-Queen problem
    solutions = solveNQueens(N)

    if solutions:
        for idx, solution in enumerate(solutions, start=1):
            print(f"Solution {idx}:")
            print_solution(solution)
    else:
        print("No solution exists for N =", N)


# Run the program
if __name__ == "__main__":
    main()
