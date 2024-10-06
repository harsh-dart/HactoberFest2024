/*
LEETCODE PROBELM 
995. Minimum Number of K Consecutive Bit Flips
(hard)
Author: Anisha

Q- You are given a binary array nums and an integer k.

A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

A subarray is a contiguous part of an array.

Intuietion: 

We want to flip subarrays of size k in a binary array nums so that all elements become 1.
The question is solved keeping in mind that:

1) Flipping Impact: Flipping affects not just the current element but the next k-1 elements as well. We need to track when these flips end.
2) Tracking Flips: Use a queue to remember when each flip ends. If a flip starts at index i, it impacts elements until i + k - 1.
3) When to Flip:
Flip if the current element is 0 and we have made an even number of flips so far.
Flip if the current element is 1 and we have made an odd number of flips.
4) Edge Case: If a flip is required but there aren’t enough elements left to flip a full subarray of size k, return -1.

APPROACH

1) Tracking where ongoing flips end using a queue.
2) for each element, remove expired flips.
   If the current element needs flipping, check if a flip is possible.
3) If flipping is needed, mark the end of the flip in the queue and increase the flip count.
4) If flipping isn't possible, return -1.
5) After iterating, return the total number of flips.

Time COMPLEXITY:
    O(n)

SPACE COMPLEXITY
    O(x)
    here x is the size of the subarray that we can flip at any given time

I hope its easy to understand from this explanation!
Thanks
*/

#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int minKBitFlips(vector<int>& nums, int k) {
        int n = nums.size();
        queue<int> flipEnds;
        int flips = 0;

        for (int i = 0; i < n; ++i) {
            if (!flipEnds.empty() && flipEnds.front() <= i) {
                flipEnds.pop();
            }
            if ((nums[i] == 0 && flipEnds.size() % 2 == 0) || (nums[i] == 1 && flipEnds.size() % 2 != 0)) {
                if (i + k > n) {
                    return -1;
                }
                flipEnds.push(i + k);
                flips++;
            }
        }
        return flips;
    }
};
