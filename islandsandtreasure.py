from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        def update(grid, r, c, distance, visited):
            grid[r][c] = min(grid[r][c], distance)

            for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                if 0 <= x + r < rows and 0 <= y + c < cols and grid[x+r][y+c] != -1 and (x+r,y+c) not in visited:
                    visited.append((x+r,y+c))
                    update(grid, x + r, y + c, distance + 1, visited)
                    visited.pop()
                 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited = [(r,c)]
                    update(grid, r, c, 0, visited)
