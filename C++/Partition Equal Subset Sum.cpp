#include <bits/stdc++.h>
using namespace std;

// Function to determine if the array can be partitioned into two subsets with equal sum
bool canPartition(vector<int>& nums) {
    int total = accumulate(nums.begin(), nums.end(), 0);
    if(total % 2 != 0) return false;
    int target = total / 2;
    vector<bool> dp(target + 1, false);
    dp[0] = true;
    for(auto num : nums){
        for(int i = target; i >= num; i--){
            dp[i] = dp[i] || dp[i - num];
        }
    }
    return dp[target];
}

int main(){
    int n;
    cout << "Enter the number of elements in the set: ";
    cin >> n;
    vector<int> nums(n);
    cout << "Enter the elements of the set: ";
    for(auto &x: nums) cin >> x;
    if(canPartition(nums))
        cout << "The array can be partitioned into two subsets with equal sum." << endl;
    else
        cout << "The array cannot be partitioned into two subsets with equal sum." << endl;
    return 0;
}
