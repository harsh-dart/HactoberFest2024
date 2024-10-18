class Solution {
public:
    // Function to check if a string has duplicate characters using bitmask
    int stringToBitmask(const string &s) {
        int mask = 0;
        for (char ch : s) {
            int bit = ch - 'a'; // Calculate bit position for character
            if (mask & (1 << bit)) {  // If the bit is already set, duplicate found
                return -1; // Return -1 if duplicate character is found
            }
            mask |= (1 << bit); // Set the bit corresponding to the character
        }
        return mask; // Return the computed bitmask
    }

    // Recursive function to find the maximum length of unique characters
    int solve(int i, const vector<int>& masks, int currentMask) {
        if (i >= masks.size()) {
            return __builtin_popcount(currentMask); // Count the number of set bits (length of unique chars)
        }

        // Exclude the current string
        int exclude = solve(i + 1, masks, currentMask);

        // Include the current string if there are no common characters
        int include = 0;
        if (masks[i] != -1 && (currentMask & masks[i]) == 0) {
            include = solve(i + 1, masks, currentMask | masks[i]); // Include current string
        }

        return max(include, exclude); // Return the maximum length
    }

    int maxLength(vector<string>& arr) {
        vector<int> masks(arr.size());
        
        // Precompute bitmasks for all strings and eliminate those with duplicate characters
        for (int i = 0; i < arr.size(); ++i) {
            masks[i] = stringToBitmask(arr[i]);
        }

        // Start recursive solving with an empty mask (0)
        return solve(0, masks, 0);
    }
};
