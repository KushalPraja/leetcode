from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        rows = len(matrix)
        columns = len(matrix[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        subarr = []

        def dfs(r,c, rows, columns):
            nonlocal subarr
            if rows - r <= 1 or columns - c <= 1:
                for i in [row[c:columns] for row in matrix[r:rows]]:
                    for j in i:
                        subarr.append(j)
                return

            initial_r, initial_c = r, c
            for x,y in directions:
                while initial_r <= r + x < rows and initial_c <= c + y < columns:
                    subarr.append(matrix[r][c])
                    r += x
                    c += y
            
            dfs(r + 1, c + 1, rows - 1, columns - 1)
                
        
        dfs(0,0, rows, columns)
        return subarr
                