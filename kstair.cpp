#include <iostream>
#include <vector>

int countWays(int k) {
    if (k <= 1) return 1; // Base case: 1 way to reach 0th or 1st stair

    std::vector<int> ways(k + 1);
    ways[0] = 1; // 1 way to stay at ground (0th stair)
    ways[1] = 1; // 1 way to reach 1st stair

    for (int i = 2; i <= k; ++i) {
        ways[i] = ways[i - 1] + ways[i - 2]; // Sum of ways to reach the previous two stairs
    }

    return ways[k]; // Return the number of ways to reach the k-th stair
}

int main() {
    int k;
    std::cout << "Enter the number of stairs (K): ";
    std::cin >> k;

    int result = countWays(k);
    std::cout << "Number of ways to reach the " << k << "th stair: " << result << std::endl;

    return 0;
}
