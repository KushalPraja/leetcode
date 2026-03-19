from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        
        count = 0
        temp_grid = [[0] * len(grid[0]) for _ in range(len(grid))] 
        x_count = [[0] * len(grid[0]) for _ in range(len(grid))] 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "X":
                    temp_grid[i][j] = 1
                    x_count[i][j] = 1
                elif grid[i][j] == "Y":
                    temp_grid[i][j] = -1
                else:
                    temp_grid[i][j] = 0

                if i > 0:
                    temp_grid[i][j] += temp_grid[i-1][j]
                    x_count[i][j] += x_count[i-1][j]
                if j > 0:
                    temp_grid[i][j] += temp_grid[i][j-1]
                    x_count[i][j] += x_count[i][j-1]
                if i > 0 and j > 0:
                    temp_grid[i][j] -= temp_grid[i-1][j-1]
                    x_count[i][j] -= x_count[i-1][j-1]

                if temp_grid[i][j] == 0 and x_count[i][j] > 0:
                    count +=1 
        
        return count