def solveNQueens(N):
    def backtrack(row, columns, diagonals1, diagonals2, board):
        if row == N:
            result.append(board)
            return
        
        for col in range(N):
            if col in columns or (row - col) in diagonals1 or (row + col) in diagonals2:
                continue
            
            # Place the queen
            columns.add(col)
            diagonals1.add(row - col)
            diagonals2.add(row + col)
            new_board = board + ["." * col + "Q" + "." * (N - col - 1)]
            
            backtrack(row + 1, columns, diagonals1, diagonals2, new_board)
            
            # Remove the queen (backtrack)
            columns.remove(col)
            diagonals1.remove(row - col)
            diagonals2.remove(row + col)

    result = []
    backtrack(0, set(), set(), set(), [])
    return result

# Example Usage
N = 4
solutions = solveNQueens(N)
for solution in solutions:
    for row in solution:
        print(row)
    print()  # Print a blank line between solutions
