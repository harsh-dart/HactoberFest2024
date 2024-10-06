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

    // Recursive function to find the maximum length
    int solve(int i, vector<int>& masks, int currentMask, int n, vector<string>& arr) {
        if (i >= n) 
            return __builtin_popcount(currentMask);  // Count the number of set bits (length of unique chars)
        
        int include = 0;
        int exclude = solve(i+1, masks, currentMask, n, arr);  // Exclude current string

        // If no common characters between current mask and next string's mask
        if (masks[i] != -1 && (currentMask & masks[i]) == 0) {
            include = solve(i+1, masks, currentMask | masks[i], n, arr);  // Include current string
        }

        return max(include, exclude);
    }

    int maxLength(vector<string>& arr) {
        int n = arr.size();
        vector<int> masks(n, 0);
        
        // Precompute bitmasks for all strings and eliminate those with duplicate characters
        for (int i = 0; i < n; ++i) {
            masks[i] = stringToBitmask(arr[i]);
        }

        // Start recursive solving with an empty mask (0)
        return solve(0, masks, 0, n, arr);
    }
};
