class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_val = prices[0]

        for i in range(len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]

            max_profit = max(prices[i] - min_val, max_profit)
       
        return max_profit

prices = [10,1,5,6,7,1]
print(Solution().maxProfit(prices))
