from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Step 1: Sort the skill array
        skill.sort()
        
        # Required sum for each pair based on the first and last player after sorting
        total_skill = skill[0] + skill[-1]  
        chemistry_sum = 0

        # Step 2: Pair players using a two-pointer approach
        n = len(skill)
        for i in range(n // 2):
            # Check if the sum of current pair matches the required total_skill
            if skill[i] + skill[n - i - 1] != total_skill:
                return -1  # Invalid configuration, return -1
            
            # Calculate the chemistry (product of the pair) and add it to the sum
            chemistry_sum += skill[i] * skill[n - i - 1]

        return chemistry_sum  # Return total chemistry
