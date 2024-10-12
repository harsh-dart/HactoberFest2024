#include <bits/stdc++.h>
using namespace std;

// Function to find the maximum subarray sum using Kadane's Algorithm
int maxSubArray(vector<int>& nums) {
    if(nums.empty()) return 0;
    int maxSum = nums[0], currentSum = nums[0];
    for(int i = 1; i < nums.size(); i++) {
        currentSum = max(nums[i], currentSum + nums[i]);
        maxSum = max(maxSum, currentSum);
    }
    return maxSum;
}

int main(){
    int n;
    cout << "Enter the number of elements in the array: ";
    cin >> n;
    vector<int> nums(n);
    cout << "Enter the elements of the array: ";
    for(auto &x: nums) cin >> x;
    cout << "Maximum Subarray Sum = " << maxSubArray(nums) << endl;
    return 0;
}
