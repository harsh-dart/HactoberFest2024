import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> results = new ArrayList<>();
        findCombinations(0, target, candidates, new ArrayList<>(), results);
        return results;
    }

    private void findCombinations(int startIndex, int remainingTarget, int[] candidates, List<Integer> currentCombination, List<List<Integer>> results) {
        // Base case: If the remaining target is zero, we found a valid combination
        if (remainingTarget == 0) {
            results.add(new ArrayList<>(currentCombination));
            return;
        }
        
        // Iterate over candidates starting from startIndex
        for (int i = startIndex; i < candidates.length; i++) {
            // If the candidate is greater than the remaining target, skip it
            if (candidates[i] > remainingTarget) {
                continue; // (Optional) Early exit for optimization if candidates are sorted
            }

            // Include the candidate and explore further
            currentCombination.add(candidates[i]);
            findCombinations(i, remainingTarget - candidates[i], candidates, currentCombination, results); // Not incrementing i allows the same element to be reused
            currentCombination.remove(currentCombination.size() - 1); // Backtrack
        }
    }
}
