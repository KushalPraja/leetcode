from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = {}
        def dfs(cn:int):
            nonlocal coins
            if cn == 0:
                return 0
            
            if cn in cache:
                return cache[cn]

            min_coins = float('inf')
            for i in range(len(coins)):
                if cn - coins[i] >= 0:
                    min_coins = min(min_coins, 1 + dfs(cn - coins[i]))
            
            cache[cn] = min_coins
            return min_coins

        x = dfs(amount) 
        
        if x == float('inf'):
            return -1 
            
        return int(x)


# dp appraoch

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        dp = [float('inf')] * (amount + 1)

        for i in coins:
            if i < len(dp):
                dp[i] = 1
        
        dp[0] = 0

        for i in range(len(dp)):
            for j in coins:
                if i - j >= 0:
                    dp[i] = min(dp[i- j] + 1, dp[i])

        return dp[-1] if dp[-1] != float('inf') else -1

