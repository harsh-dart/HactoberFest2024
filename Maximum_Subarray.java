class Solution {
    public int maxSubArray(int[] nums) {
        int len = nums.length;
        int currentMax = 0;
        int max = Integer.MIN_VALUE;
        
        for(int i:nums){
            currentMax += i;
            if(max < currentMax){
                max = currentMax;
            }
            if(currentMax < 0){
                currentMax = 0;
            }
        }
        return max;
    }
}
