from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        visited = set([]) 

        def dfs(i, j, prev):
            print(grid[i][j])
            if grid[i][j] == -1:
                return True
            
            curr = grid[i][j]
            visited.add((i,j))
            
            for dx, dy in [(1,0), (0,1), (-1,0), (0, -1)]:
                if (0 <= i + dx < len(grid) and 0 <= j + dy < len(grid[0])) and (-dx, -dy) != prev:
                    if grid[i + dx][j + dy] == curr or grid[i + dx][j + dy] == -1:
                        grid[i][j] = -1
                        if dfs(i + dx, j + dy,(dx, dy)):
                            return True
                        grid[i][j] = curr
            
            return False

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited:
                    if dfs(i, j, None):
                        return True

        return False

                    

