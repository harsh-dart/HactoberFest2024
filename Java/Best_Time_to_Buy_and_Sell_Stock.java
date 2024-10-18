class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int minValue = Integer.MAX_VALUE; // Use Integer.MAX_VALUE for better clarity

        for (int i = 0; i < prices.length; i++) {
            if (minValue > prices[i]) {
                minValue = prices[i];
            }
            if (maxProfit < prices[i] - minValue) {
                maxProfit = prices[i] - minValue;
            }
        }
        return maxProfit;
    }
}

public class HelloWorld {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Example input
        int[] prices = {7, 1, 5, 3, 6, 4};
        int profit = solution.maxProfit(prices);
        
        System.out.println("Maximum profit: " + profit);
    }
}
