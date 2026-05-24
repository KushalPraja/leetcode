from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
       
       
        queue = deque([])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append(((i,j), 0))

        max_count = 0

        while queue:
            temp = queue.popleft()
            curr, count = temp
            curr_x, curr_y = curr

            directions =  [(1,0), (0,1), (0,-1), (-1,0)]

            for nx, ny  in directions:
                if 0 <= curr_x + nx < len(grid) and 0<= curr_y + ny < len(grid[0]):
                    if grid[curr_x + nx][curr_y + ny] == 1:
                        grid[curr_x + nx][curr_y + ny] = 2
                        queue.append(((curr_x + nx,curr_y + ny), count + 1))
                        max_count = max(max_count, count + 1) 
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return max_count


