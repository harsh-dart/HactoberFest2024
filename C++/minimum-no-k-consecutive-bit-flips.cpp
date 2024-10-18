#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int minKBitFlips(vector<int>& nums, int k) {
        int n = nums.size();
        queue<int> flipEnds; // To track when flips end
        int flips = 0; // Count of flips
        int currentFlips = 0; // Current number of active flips

        for (int i = 0; i < n; ++i) {
            // Remove expired flips
            if (!flipEnds.empty() && flipEnds.front() <= i) {
                flipEnds.pop();
                currentFlips--; // Decrease the active flips count
            }

            // Determine if we need to flip at this index
            bool isFlipped = currentFlips % 2 == 1; // Check if the current index is flipped
            if ((nums[i] == 0 && !isFlipped) || (nums[i] == 1 && isFlipped)) {
                if (i + k > n) {
                    return -1; // Not enough elements left to flip
                }
                flipEnds.push(i + k); // Mark when the flip ends
                currentFlips++; // Increase the active flips count
                flips++; // Increase the total flips count
            }
        }
        
        return flips; // Return the total number of flips
    }
};
