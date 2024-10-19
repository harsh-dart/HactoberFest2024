import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] arr, int target) {
        int len = arr.length;
        int[] res = new int[2];
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < len; i++) {
            int complement = target - arr[i];
            if (map.containsKey(complement)) {
                res[0] = map.get(complement);
                res[1] = i;
                return res;
            }
            map.put(arr[i], i);
        }
        return res; // Optionally handle cases where no solution is found
    }
}
