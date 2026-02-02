from typing import List

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        ROWS, COLS = len(maze), len(maze[0])
        visited = set()

        def dfs(x, y):
            if (x, y) in visited:
                return False
            if [x, y] == destination:
                return True

            visited.add((x, y))

            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x, y
                while 0 <= nx + dx < ROWS and 0 <= ny + dy < COLS and maze[nx + dx][ny + dy] == 0:
                    nx += dx
                    ny += dy

                if dfs(nx, ny):
                    return True

            return False

        return dfs(start[0], start[1])

