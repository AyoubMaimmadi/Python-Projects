def coinsNum(list, n):
    dp = [n+1] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in list: 
            if i - j >= 0: 
                dp[i] = min(dp[i], 1 + dp[i - j])
    return dp[n] if dp[n] != n + 1 else -1
    
nums = [1,3,4,5]
print(coinsNum(nums, 7))



             



