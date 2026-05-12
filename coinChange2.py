from typing import List


# top down approach with memoization
class Solution:
    def Memo_change(self, amount: int, coins: List[int]) -> int:

        vis = {}
        coins.sort()

        def dfs(start, rem):
            if rem == 0:
                return 1

            if (start, rem) in vis:
                return vis[(start, rem)]

            ways = 0

            for i in range(start, len(coins)):
                if coins[i] > rem:
                    break
                ways += dfs(i, rem - coins[i])

            vis[(start, rem)] = ways
            return ways

        return dfs(0, amount)


    # bottom up apporach [using 0-1 knapsack approach]

    def Bot_change(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]

    # My approach (similar to 0-1 knapsack but we can use the same coin multiple times)
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for i in range(len(coins)):
            if coins[i] <= amount:
                dp[coins[i]] = 1 


        coins = set(coins)
        for i in range(1, amount + 1):
            min_way = float('inf')

            for j in coins:
                rem = i - j
                if rem >= 0 and dp[rem] != -1:
                    min_way = min(dp[rem] + 1, min_way)
            
            if min_way == float('inf'):
                dp[i] = -1
            
            else:
                dp[i] = min_way

        return dp[-1]