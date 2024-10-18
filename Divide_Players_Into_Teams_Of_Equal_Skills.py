from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Step 1: Check for odd number of players
        if len(skill) % 2 != 0:
            return -1  # Invalid configuration for odd number of players
        
        # Step 2: Sort the skill array
        skill.sort()
        
        total_skill = skill[0] + skill[-1]  # Required sum for each pair
        chemistry_sum = 0

        # Step 3: Pair players using two pointers
        for i in range(len(skill) // 2):
            # Check if the sum of current pair matches the required total_skill
            if skill[i] + skill[-i - 1] != total_skill:
                return -1  # Invalid configuration, return -1
            # Calculate the chemistry (product of pair) and add it to the sum
            chemistry_sum += skill[i] * skill[-i - 1]

        return chemistry_sum  # Return total chemistry
    
if __name__ == "__main__":
    solution = Solution()
    skill = [3,2,5,1]

    result = solution.dividePlayers(skill)
    print(f"The total chemistry is:{result}")
