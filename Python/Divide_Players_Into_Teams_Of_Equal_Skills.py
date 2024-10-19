from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Step 1: Sort the skill array
        skill.sort()
        
        # Step 2: Calculate the required sum for each pair
        total_skill = skill[0] + skill[-1]  
        chemistry_sum = 0

        # Step 3: Pair players using two pointers
        n = len(skill)
        for i in range(n // 2):
            # Check if the sum of the current pair matches the required total_skill
            if skill[i] + skill[n - 1 - i] != total_skill:
                return -1  # Invalid configuration, return -1
            
            # Calculate the chemistry (product of pair) and add it to the sum
            chemistry_sum += skill[i] * skill[n - 1 - i]

        # Step 4: Return total chemistry
        return chemistry_sum
