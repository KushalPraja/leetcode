from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_curr = prices[0]
        total = 0

        for i in range(1, len(prices)):
            
            if prices[i] <= min_curr:
                min_curr = prices[i]

            elif prices[i] > min_curr:
                total += prices[i] - min_curr
                min_curr = prices[i]

        return total
