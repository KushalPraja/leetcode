from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        
        count = 0
        rows, cols = len(grid), len(grid[0])
        temp_grid = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                temp_grid[i][j] = grid[i][j]

                if  0<= j- 1 < cols and 0 <= i - 1 < rows and temp_grid[i][j-1] and temp_grid[i-1][j]:
                    temp_grid[i][j] += temp_grid[i][j-1] + temp_grid[i-1][j] - temp_grid[i-1][j-1]
                
                elif 0<= j-1 < cols and temp_grid[i][j-1]:
                    temp_grid[i][j] += temp_grid[i][j - 1]
                
                elif 0 <= i-1 < rows and temp_grid[i-1][j]: 
                    temp_grid[i][j] += temp_grid[i - 1][j]

                if temp_grid[i][j] <= k:
                    count += 1

        return count

