from typing import List

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        
        t = x
        r = x + (k - 1)

        while (t < r):
            for i in range(y, y + k):
                grid[t][i], grid[r][i] = grid[r][i], grid[t][i]

            t += 1
            r -= 1

        return grid
