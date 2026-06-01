from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:

        cost.sort()
        total = 0

        if len(cost) < 3:
            return sum(cost)

        for i in range(len(cost) - 1, -1, -3):
            total += cost[i]

            if i > 0:
                total += cost[i - 1]
            
        return total



           