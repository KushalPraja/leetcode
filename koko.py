import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while (left < right):
            mid = (right + left)//2

            tm = 0

            for i in piles:
                x = math.ceil(i/mid)
                tm += x
            
            if tm <= h:
                right = mid 
            
            elif tm > h:
                left = mid + 1
    
        return (left + right)//2


if __name__ == '__main__':
    sol = Solution()
    print(sol.minEatingSpeed([1,2,3,4,5,6,7,8,9], 10))
