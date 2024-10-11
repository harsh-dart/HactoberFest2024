import java.util.Scanner;

public class Staircase {

    public static int countWaysToReachStair(int K) {
        if (K == 0 || K == 1) {
            return 1;
        }

        int[] dp = new int[K + 1];
        dp[0] = 1;  // 1 way to stay at step 0
        dp[1] = 1;  // 1 way to reach step 1

        for (int i = 2; i <= K; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];  // Sum of ways to reach (i-1) and (i-2)
        }

        return dp[K];
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the value of K (stair number): ");
        int K = scanner.nextInt();

        if (K < 0) {
            System.out.println("Invalid input! K must be non-negative.");
            return;
        }

        System.out.println("Number of ways to reach the " + K + "-th stair: " + countWaysToReachStair(K));
    }
}
