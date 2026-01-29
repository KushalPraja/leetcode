from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area = 0
        length = 0

        rows, cols = len(grid), len(grid[0])

        def dfs(grid, r, c):
            # make this one visited 
            nonlocal length
            grid[r][c] = 0
            length += 1

            for x, y in [(1,0), (0,1), (-1, 0), (0,-1)]:
                if 0 <= x + r < rows and 0<= y + c < cols and grid[x+r][y+c] == 1:
                    dfs(grid, x+r , y+c)
            return 
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    length = 0
                    dfs(grid, r, c)
                    max_area = max( length, max_area)

        return max_area
