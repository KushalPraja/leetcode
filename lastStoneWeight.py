from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if  len(stones) <= 1:
            if len(stones) != 1:
                return 0
            return stones[0]

        stones = sorted(stones)
        first = stones[-1]
        stones.pop()
        second = stones[-1]
        stones.pop()

        if first != second:
            stones.insert(0, abs(second-first))

        return self.lastStoneWeight(stones)
    
