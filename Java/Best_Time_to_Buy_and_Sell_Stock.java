class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int minValue = 100001;
        for(int i=0;i<prices.length; i++){
           if(minValue > prices[i]){
               minValue = prices[i];
           }
            if(maxProfit < prices[i] - minValue){
                maxProfit = prices[i] - minValue;
            }
        }
        return maxProfit;
    }
}

//Second approach
class Solution {
    public int maxProfit(int[] prices) {
        int buy = prices[0];
        int profit = 0;
        for(int i=1;i<prices.length;i++){
            if(prices[i] < buy)
                buy = prices[i];
            profit = Math.max(profit, prices[i]-buy);
        }
        return profit;
    }
}
