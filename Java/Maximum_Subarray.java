class Solution {
    public int maxSubArray(int[] nums) {
        int currentMax = 0;
        int max = Integer.MIN_VALUE; // Initialize max to the lowest possible integer
        
        for (int i : nums) {
            currentMax += i; // Add the current number to the current maximum sum
            
            if (max < currentMax) {
                max = currentMax; // Update max if the current maximum is larger
            }
            
            if (currentMax < 0) {
                currentMax = 0; // Reset currentMax if it drops below 0
            }
        }
        
        return max; // Return the maximum subarray sum
    }
}

public class HelloWorld {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Example usage
        int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        int maxSum = solution.maxSubArray(nums);
        
        System.out.println("Maximum subarray sum: " + maxSum); // Output the result
    }
}
