from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0]);
        island_count = 0;

        def updateneighbours(r, c):
                
            # mark as visited
            grid[r][c] = "0"

            for (x,y) in [(1,0), (0,1), (0,-1), (-1,0)]:
                if 0<= r + x < rows and 0 <= c + y < cols and grid[r+x][c+y] == "1":
                    updateneighbours(r+x, c+y);

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1
                    updateneighbours(r,c)

        return island_count



