
public class NQueen {

    public static boolean isSafe(char[][] arr, int row, int col) {
        int N = arr.length;

        // Check vertical above
        for (int i = 0; i < row; i++) {
            if (arr[i][col] == 'Q') {
                return false;
            }
        }
        for (int i = 0; i < col; i++) {
            if (arr[row][i] == 'Q') {
                return false;
            }
        }

        // Check upper left diagonal
        for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (arr[i][j] == 'Q') {
                return false;
            }
        }

        // Check upper right diagonal
        for (int i = row, j = col; i >= 0 && j < N; i--, j++) {
            if (arr[i][j] == 'Q') {
                return false;
            }
        }
        //lower left
        for (int i = row, j = col; i < N && j >= 0; i++, j--) {
            if (arr[i][j] == 'Q') {
                return false;
            }
        }

        // Check lower right diagonal
        for (int i = row, j = col; i < N && j < N; i++, j++) {
            if (arr[i][j] == 'Q') {
                return false;
            }
        }

        return true;
    }

    public static void printQueen(char[][] arr, int col) {
        int N = arr.length;
        if (col == N) {
            printResult(arr);
            System.out.println();
            return;
        }

        for (int i = 0; i < N; i++) {
            if (isSafe(arr, i, col)) {
                arr[i][col] = 'Q';
                printQueen(arr, col + 1);
                arr[i][col] = '.';
            }
        }
    }

    public static void printResult(char[][] arr) {
        int N = arr.length;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int N = 4;
        char[][] arr = new char[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                arr[i][j] = '.';
            }
        }
        printQueen(arr, 0);
    }
}
