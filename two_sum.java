class Solution {
    public int[] twoSum(int[] arr, int target) {
        int len = arr.length;
        int[] res = new int[2];
        HashMap map = new HashMap<Integer,Integer>();
        
        for(int i=0; i < len; i++){
            if(map.containsKey(target - arr[i])){
                res[0] = (int) map.get(target - arr[i]);
                res[1] = i;
                return res;
            }
            map.put(arr[i],i);
        }
        return res;
    }
}
