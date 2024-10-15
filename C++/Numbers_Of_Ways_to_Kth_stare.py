def numberOfWays(k: int) -> int:
    # dp[i] will store the number of ways to reach stair i
    dp = [0] * (k + 1)
    
    # Base case: 1 way to reach the first stair
    dp[1] = 1
    
    # Iterate over each stair up to k
    for i in range(1, k):
        jump = 0
        stair = i
        # Keep jumping upwards as long as within bounds
        while stair <= k:
            if stair <= k:
                dp[stair] += dp[i]
            jump += 1
            stair = i + 2**jump
    
    return dp[k]

# Test the function
k = 10  # example value
print(numberOfWays(k))
