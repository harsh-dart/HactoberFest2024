#include <iostream>
#include <vector>

int findWays(int k) {
    if (k <= 1) return 1;

    std::vector<int> dp(k + 1);
    dp[0] = 1;  // One way to stay on the ground
    dp[1] = 1;  // One way to reach the first stair

    for (int i = 2; i <= k; i++) {
        dp[i] = dp[i - 1] + dp[i - 2]; // Ways to reach current stair
    }

    return dp[k];
}

int main() {
    int k;
    std::cout << "Enter the number of stairs (K): ";
    std::cin >> k;

    int ways = findWays(k);
    std::cout << "Number of ways to reach the " << k << "-th stair: " << ways << std::endl;

    return 0;
}

