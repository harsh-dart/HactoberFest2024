import java.util.HashMap;

class Solution {
    HashMap<String, Integer> mem = new HashMap<>();

    public int waysToReachStair(int k) {
        return dfs(1, 0, false, k);
    }

    private int dfs(int cur, int jump, boolean back, int k) {
        String key = cur + "_" + jump + "_" + back;
        if (mem.containsKey(key)) {
            return mem.get(key);
        }

        int ways = 0;
        if (cur == k && (back || cur == 0) && jump > 0) {
            return 1;
        }

        else if (cur == k) {
            ways++;
        }

        if (cur < 0) {
            return 0;
        }

        int nxt = cur + (1 << jump);
        if (nxt <= k + 1) {
            ways += dfs(nxt, jump + 1, false, k);
        }

        if (cur > 0 && !back) {
            ways += dfs(cur - 1, jump, true, k);
        }

        mem.put(key, ways);
        return ways;
    }
}
