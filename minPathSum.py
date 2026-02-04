from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        cache = {}

        def dfs(r, c):

            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return grid[r][c]

            if (r, c) in cache:
                return cache[(r,c)]
            
            min_path = float('inf')
            for x, y in [(1,0), (0,1)]:
                if 0 <= r + x < len(grid) and 0 <= c + y < len(grid[0]):
                    min_path= min(grid[r][c] + dfs(r + x, c + y), min_path)
            
            cache[(r,c)] = min_path
            return min_path
        
        x = dfs(0, 0)

        if x == float('inf'):
            return 0

        else:
            return int(x)
    
