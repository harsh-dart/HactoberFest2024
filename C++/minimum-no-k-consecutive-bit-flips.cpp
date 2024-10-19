#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int minKBitFlips(vector<int>& nums, int k) {
        int n = nums.size();
        queue<int> flipEnds; // To track when flips end
        int flips = 0; // Counter for the number of flips

        for (int i = 0; i < n; ++i) {
            // Remove expired flips
            if (!flipEnds.empty() && flipEnds.front() <= i) {
                flipEnds.pop();
            }

            // Determine if we need to flip at the current index
            bool currentFlipNeeded = (nums[i] == 0 && flipEnds.size() % 2 == 0) ||
                                      (nums[i] == 1 && flipEnds.size() % 2 != 0);
            
            if (currentFlipNeeded) {
                // Check if there are enough elements left for a flip
                if (i + k > n) {
                    return -1;
                }
                flipEnds.push(i + k); // Mark the end of the flip
                flips++; // Increment flip count
            }
        }

        return flips; // Return the total number of flips
    }
};

