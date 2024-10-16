class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Step 1: Sort the skill array
        skill.sort()

        # Initialize pointers and the required chemistry sum
        left, right = 0, len(skill) - 1
        total_skill = skill[left] + skill[right]  # Target sum for each pair
        chemistry_sum = 0

        # Step 2: Pair players using two pointers
        while left < right:
            current_sum = skill[left] + skill[right]
            if current_sum != total_skill:
                return -1  # Invalid configuration, return -1
            chemistry_sum += skill[left] * skill[right]  # Calculate chemistry
            left += 1
            right -= 1

        return chemistry_sum  # Return total chemistry
