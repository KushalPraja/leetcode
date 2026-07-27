from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        

        m = len(grid)
        n = len(grid[0])
        queue = deque([])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append(((i,j), 0))

        while queue:
            coords, level = queue.popleft()
            i, j = coords

            for nx, ny in [(1,0), (0,1), (-1,0), (0,-1)]:
                if 0 <= nx + i < m and 0 <= ny + j < n and grid[nx + i][ny + j] == 2147483647:
                    grid[nx + i][ny + j] = level + 1
                    queue.append(((nx + i, ny + j), level + 1))

        