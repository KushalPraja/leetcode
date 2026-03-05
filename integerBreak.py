class Solution:
    def integerBreak(self, n: int) -> int:
        
        dp = [0] * (n + 1)
        dp[2] = 2

        if n == 2:
            return 1
        
        dp[3] = 3
        
        if n == 3:
            return 2

        for i in range(4, len(dp)):
            dp[i] = max(2 * dp[i-2], 3 * dp[i - 3])
        
        return dp[-1]

