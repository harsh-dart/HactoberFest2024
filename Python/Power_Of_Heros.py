from typing import List

class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        ans, t, base = 0, 0, 10**9 + 7
        
        # Iterate over the sorted 'nums' list
        for c in sorted(nums):
            # Calculate the power contribution of the current element 'c'
            ans = (ans + (t + c) * c * c) % base
            
            # Update 't' for the next iteration
            t = (2 * t + c) % base
        
        return ans  # Return the final sum of powers modulo 10^9 + 7
