import java.util.HashMap;

public class ReachKthStair {

    // HashMap to store already computed results (memoization)
    private static HashMap<String, Long> memo = new HashMap<>();

    public static long findWays(int k) {
        return calculateWays(1, 0, k);
    }

    // Recursive function to calculate the number of ways to reach the k-th stair
    private static long calculateWays(int currentStair, int jump, int k) {
        // If we reached the k-th stair, count as 1 way
        if (currentStair == k) return 1;
        
        // If we exceeded the k-th stair, no valid path
        if (currentStair > k) return 0;

        // Memoization key (combination of current stair and jump)
        String key = currentStair + "," + jump;

        // If the result is already computed, return it
        if (memo.containsKey(key)) return memo.get(key);

        // Two possible moves:
        // 1. Go down to (i - 1), but only if not consecutive down move from stair 0
        long waysToGoDown = (currentStair > 1) ? calculateWays(currentStair - 1, 0, k) : 0;

        // 2. Go up to (i + 2^jump) and increase jump
        long waysToGoUp = calculateWays(currentStair + (int) Math.pow(2, jump), jump + 1, k);

        // Total ways from current stair
        long totalWays = waysToGoDown + waysToGoUp;

        // Store the result in the memo map
        memo.put(key, totalWays);

        return totalWays;
    }

    public static void main(String[] args) {
        int k = 5; // Example value for k
        System.out.println("Total ways to reach the " + k + "-th stair: " + findWays(k));
    }
}
