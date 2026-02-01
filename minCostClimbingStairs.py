from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        path = [0] * len(cost)
        path[0]  = cost[0]
        path[1] = cost[1]

        for i in range(2, len(path)):
            path[i] = cost[i] + min(path[i -1], path[i-2])

        print(path)
        return min(path[-1], path[-2])

