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


    # bottom up apporach

    def Bot_change(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
