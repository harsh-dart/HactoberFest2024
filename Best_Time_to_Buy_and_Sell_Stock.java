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
