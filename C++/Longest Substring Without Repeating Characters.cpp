class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.empty()) return 0;

        unordered_map<char, int> lastSeen; // Tracks the last seen index of characters
        int maxLength = 0;
        int start = 0; // Left boundary of the sliding window

        for (int end = 0; end < s.size(); ++end) {
            char currentChar = s[end];

            // If the character is already in the map and within the current window
            if (lastSeen.find(currentChar) != lastSeen.end() && lastSeen[currentChar] >= start) {
                // Move the start to the right of the last seen position
                start = lastSeen[currentChar] + 1;
            }

            // Update the last seen position of the current character
            lastSeen[currentChar] = end;

            // Update the maxLength if the current window is larger
            maxLength = max(maxLength, end - start + 1);
        }

        return maxLength;
    }
};
