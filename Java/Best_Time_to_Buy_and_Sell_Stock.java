class Solution {
    public int maxProfit(int[] prices) {
        // Return 0 if the prices array is empty
        if (prices.length == 0) {
            return 0;
        }

        int maxProfit = 0;
        int minValue = prices[0]; // Initialize to the first price

        for (int i = 1; i < prices.length; i++) {
            // Update minValue if current price is lower
            if (prices[i] < minValue) {
                minValue = prices[i];
            } else {
                // Calculate potential profit and update maxProfit if it's higher
                maxProfit = Math.max(maxProfit, prices[i] - minValue);
            }
        }
        
        return maxProfit;
    }
}
