// this was the most common and highlt asked problem on FAANG Interviews from Leetcode
// Approach - BackTracking 

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<Integer> active = new ArrayList<>();
        List<List<Integer>> ans = new ArrayList<>();
        helper(0, target, candidates, active, ans);
        return ans;
    }

    static void helper(int index, int target, int[] candidates, List<Integer> active, List<List<Integer>> ans) {
        // Base case: If target is reached, add the current combination to the answer list
        if (target == 0) {
            ans.add(new ArrayList<>(active));
            return;
        }

        // If we have considered all candidates
        if (index == candidates.length) {
            return;
        }

        // If the candidate can be included in the combination
        if (candidates[index] <= target) {
            active.add(candidates[index]); // Include the candidate
            helper(index, target - candidates[index], candidates, active, ans); // Recur with updated target
            active.remove(active.size() - 1); // Backtrack
        }

        // Exclude the current candidate and move to the next
        helper(index + 1, target, candidates, active, ans);
    }
}
