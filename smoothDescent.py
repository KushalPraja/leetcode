from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        dp = [1] * len(prices)

        for i in range(len(prices)):
            if i > 0 and prices[i-1] - prices[i] == 1:
                dp[i] = dp[i-1] + 1
        
        return sum(dp)
