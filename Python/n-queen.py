def solve_n_queens(N):
    def is_not_under_attack(row, col):
        return (col not in cols) and (row - col not in diag1) and (row + col not in diag2)

    def place_queen(row, col):
        queens[row] = col
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)

    def remove_queen(row, col):
        queens[row] = -1
        cols.remove(col)
        diag1.remove(row - col)
        diag2.remove(row + col)

    def add_solution():
        solution = []
        for i in range(N):
            row = ['.'] * N
            row[queens[i]] = 'Q'
            solution.append("".join(row))
        results.append(solution)

    def backtrack(row):
        if row == N:
            add_solution()
            return
        for col in range(N):
            if is_not_under_attack(row, col):
                place_queen(row, col)
                backtrack(row + 1)
                remove_queen(row, col)

    results = []
    cols = set()
    diag1 = set()
    diag2 = set()
    queens = [-1] * N
    backtrack(0)
    return results

# Example usage:
if __name__ == "__main__":
    N = int(input("Enter the number of queens (1 <= N <= 10): "))
    solutions = solve_n_queens(N)
    print("Output:")
    for solution in solutions:
        print(solution)

