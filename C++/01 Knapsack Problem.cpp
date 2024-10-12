#include <bits/stdc++.h>
using namespace std;

// Function to solve the 0/1 Knapsack problem using Tabulation
int knapsack(int W, vector<int> &wt, vector<int> &val, int N) {
    vector<vector<int>> dp(N + 1, vector<int>(W + 1, 0));
    for(int i = 1; i <= N; i++) {
        for(int w = 1; w <= W; w++) {
            if(wt[i - 1] <= w)
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w]);
            else
                dp[i][w] = dp[i - 1][w];
        }
    }
    return dp[N][W];
}

int main(){
    int N, W;
    cout << "Enter the number of items: ";
    cin >> N;
    cout << "Enter the weights of the items: ";
    vector<int> wt(N);
    for(auto &x: wt) cin >> x;
    cout << "Enter the values of the items: ";
    vector<int> val(N);
    for(auto &x: val) cin >> x;
    cout << "Enter the capacity of the knapsack: ";
    cin >> W;
    cout << "Maximum value in Knapsack = " << knapsack(W, wt, val, N) << endl;
    return 0;
}
