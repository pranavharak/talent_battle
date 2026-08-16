def climbStairs(n):
    dp = [-1] * (n+1)
    return stairs(n,dp)
def stairs(ind,dp):
    if ind ==0 or ind == 1:
        return 1

    if dp[ind] != -1:
        return dp[ind]

    left = stairs(ind-1,dp)
    right = stairs(ind-2,dp)
    dp[ind] = left + right
    return dp[ind]    

print(climbStairs(3))