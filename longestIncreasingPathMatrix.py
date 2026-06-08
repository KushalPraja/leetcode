from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        mem = {}

        def dfs(i, j):   
            direc = [(0,1), (0,-1), (1,0), (-1,0)]
            max_len = 1

            if (i, j) in mem:
                return mem[(i, j)]

            for dx, dy in direc:
                if 0 <= i + dx < len(matrix) and 0 <= j + dy < len(matrix[0]) and matrix[i + dx][j + dy] > matrix[i][j]:
                    max_len = max(max_len, 1 + dfs(i + dx,j + dy))


            mem[(i, j)] = max_len

            return max_len

        maxlen = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                maxlen = max(dfs(i, j), maxlen)

        return maxlen
                    

