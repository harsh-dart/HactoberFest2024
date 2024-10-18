from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Step 1: Sort the skill array
        skill.sort()
        
        # Check if the number of players is odd
        if len(skill) % 2 != 0:
            return -1  # Invalid configuration, return -1
        
        total_skill = skill[0] + skill[-1]  # Required sum for each pair
        chemistry_sum = 0

        # Step 2: Pair players using two pointers
        left, right = 0, len(skill) - 1
        while left < right:
            # Check if the sum of current pair matches the required total_skill
            if skill[left] + skill[right] != total_skill:
                return -1  # Invalid configuration, return -1
            # Calculate the chemistry (product of pair) and add it to the sum
            chemistry_sum += skill[left] * skill[right]
            left += 1
            right -= 1

        return chemistry_sum  # Return total chemistry
