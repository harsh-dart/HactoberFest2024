#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    // Function to check if a string has duplicate characters using bitmask
    int stringToBitmask(const string &s) {
        int mask = 0;
        for (char ch : s) {
            int bit = ch - 'a';
            if (mask & (1 << bit))  // If the bit is already set, duplicate found
                return -1;
            mask |= (1 << bit);  // Set the bit corresponding to the character
        }
        return mask;
    }

    // Recursive function to find the maximum length of unique characters
    int solve(int i, vector<int>& masks, int currentMask, int n) {
        if (i >= n) 
            return __builtin_popcount(currentMask);  // Count the number of set bits (length of unique chars)
        
        // Exclude current string
        int exclude = solve(i + 1, masks, currentMask, n);

        // Include current string if it has no common characters with currentMask
        int include = 0;
        if (masks[i] != -1 && (currentMask & masks[i]) == 0) {
            include = solve(i + 1, masks, currentMask | masks[i], n);  // Include current string
        }

        return max(include, exclude);
    }

    int maxLength(vector<string>& arr) {
        int n = arr.size();
        vector<int> masks(n);

        // Precompute bitmasks for all strings and eliminate those with duplicate characters
        for (int i = 0; i < n; ++i) {
            masks[i] = stringToBitmask(arr[i]);
        }

        // Start recursive solving with an empty mask (0)
        return solve(0, masks, 0, n);
    }
};
