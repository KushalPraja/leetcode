from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        

        queue = deque([])

        if grid and grid[0][0] == 0:
            queue.append(((0,0), 0))

        while queue:
            curr, level = queue.popleft()

            curr_x, curr_y = curr

            if curr_x == len(grid) - 1 and curr_y == len(grid[0]) - 1:
                return level + 1

            directions = [(1,0), (0,1), (1,1), (1, -1), (-1, 1), (-1,0), (-1,-1), (0, -1)]

            for dx, dy in directions:
                if 0<= dx + curr_x < len(grid) and 0<= dy + curr_y < len(grid[0]) and grid[dx+curr_x][dy + curr_y] == 0:
                    grid[curr_x + dx][curr_y + dy] = 1
                    queue.append(((dx+curr_x,dy+curr_y), level + 1))


        return -1
