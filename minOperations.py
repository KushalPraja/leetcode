from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        
        ls = []

        rem = grid[0][0] % x

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] % x != rem:
                    return -1
                ls.append(grid[i][j])

        ls.sort()
        
        mid = len(ls) // 2

        op = 0
        for i in range(len(ls)):
            op += abs(ls[i] - ls[mid]) // x
    
        return op
