//Binary Search Algo:

public class BinarySearch {
    public static void main(String[] args) {
        int [] arr = {-212, -123, -102, -56,0,12, 29, 64, 78, 89};
        int target = 13;
        int ans = binarySearch(arr,target);
        System.out.println(ans);
    }
    static int binarySearch(int [] arr, int target) {
        int start = 0;
        int end = arr.length -1;
        while (start<=end) {
            int mid = start + (end-start)/2;

            if (target < arr[mid]) {
                end = mid-1;
            } else if (target > arr[mid]) {
                start = mid+1;
            } else {
                return mid;
            }
        }
        return -1;
    }
}
