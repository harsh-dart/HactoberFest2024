import java.util.ArrayList;
import java.util.List;

public class NQueen {

    public List<List<String>> solveNQueens(int n) {
        List<List<String>> result = new ArrayList<>();
        char[][] board = new char[n][n];

        // Initialize the board with empty spaces
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = '.';
            }
        }

        backtrack(result, board, 0, n);
        return result;
    }

    private void backtrack(List<List<String>> result, char[][] board, int row, int n) {
        // If we have placed queens in all rows, we add the solution
        if (row == n) {
            result.add(constructBoard(board));
            return;
        }

        // Try placing a queen in each column of the current row
        for (int col = 0; col < n; col++) {
            if (isValid(board, row, col, n)) {
                board[row][col] = 'Q';  // Place the queen
                backtrack(result, board, row + 1, n);  // Move to the next row
                board[row][col] = '.';  // Backtrack and remove the queen
            }
        }
    }

    // Helper function to check if it's valid to place a queen at board[row][col]
    private boolean isValid(char[][] board, int row, int col, int n) {
        // Check the column
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 'Q') {
                return false;
            }
        }

        // Check the upper-left diagonal
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }

        // Check the upper-right diagonal
        for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }

        return true;
    }

    // Helper function to convert the board to a list of strings
    private List<String> constructBoard(char[][] board) {
        List<String> currentBoard = new ArrayList<>();
        for (int i = 0; i < board.length; i++) {
            currentBoard.add(new String(board[i]));
        }
        return currentBoard;
    }

    public static void main(String[] args) {
        NQueen nQueen = new NQueen();
        int N = 4; // Example input
        List<List<String>> solutions = nQueen.solveNQueens(N);
        
        // Output all solutions
        for (List<String> solution : solutions) {
            for (String row : solution) {
                System.out.println(row);
            }
            System.out.println();
        }
    }
}

           

