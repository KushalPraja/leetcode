from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        
        layers = min(len(grid)// 2, len(grid[0]) // 2)


        for j in range(layers):
            
            arr = []

            for i in range(j, len(grid[0]) - 1 - j):
                arr.append(grid[j][i])

            for i in range(j, len(grid) - 1 - j):
                arr.append(grid[i][-1 - j])
            
            for i in range(len(grid[0]) - 1 - j, j, -1 ):
                arr.append(grid[-1 - j][i])
            
            for i in range(len(grid) - 1 - j, j, -1):
                arr.append(grid[i][j])

            n = len(arr)

            for i in range(k % n):
                x = arr[0]
                arr.pop(0)
                arr.append(x)

            for i in range(j, len(grid[0]) - 1 - j):
                x= arr[0]
                arr.pop(0)
                grid[j][i] = x

            for i in range(j, len(grid) - 1 - j):
                x= arr[0]
                arr.pop(0)
                grid[i][-1 - j] = x
           
            for i in range(len(grid[0]) - 1 - j, j, -1 ):
                x= arr[0]
                arr.pop(0)
                grid[-1 - j][i] = x
 
            for i in range(len(grid) - 1 - j, j, -1):
                x= arr[0]
                arr.pop(0)
                grid[i][j] = x

        return grid



            

