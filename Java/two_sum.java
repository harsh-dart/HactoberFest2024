import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] arr, int target) {
        // Create a HashMap to store array values and their indices
        HashMap<Integer, Integer> valueToIndexMap = new HashMap<>();
        
        // Iterate through the array
        for (int i = 0; i < arr.length; i++) {
            // Calculate the complement that we need to find
            int complement = target - arr[i];
            
            // Check if the complement exists in the HashMap
            if (valueToIndexMap.containsKey(complement)) {
                // If it exists, return the indices of the two numbers
                return new int[] { valueToIndexMap.get(complement), i };
            }
            // Store the current number and its index in the HashMap
            valueToIndexMap.put(arr[i], i);
        }
        
        // If no solution is found, throw an exception (or return an indication)
        throw new IllegalArgumentException("No two sum solution found.");
    }
}
