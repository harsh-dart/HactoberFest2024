class Solution {
    public int maxSubArray(int[] nums) {
        // Initialize current sum and maximum sum
        int currentSum = 0;
        int maxSum = Integer.MIN_VALUE; // To handle the case where all numbers are negative

        // Iterate through each number in the array
        for (int num : nums) {
            currentSum += num; // Add the current number to the current sum

            // Update maxSum if currentSum is greater
            if (currentSum > maxSum) {
                maxSum = currentSum;
            }

            // Reset currentSum to 0 if it drops below 0
            if (currentSum < 0) {
                currentSum = 0; 
            }
        }
        
        return maxSum; // Return the maximum sum found
    }
}
