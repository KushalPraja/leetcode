from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        rows = len(heights)
        cols = len(heights[0])

        pacific_set = set()
        atlantic_set = set()

        def pacific_dfs(i, j):

            curr = heights[i][j]
            pacific_set.add((i,j))
            
            for nx, ny in [(1,0), (0,1), (0,-1), (-1,0)]:
                if 0 <= i + nx < rows and 0 <= j + ny < cols and heights[i + nx][j + ny] >= curr and (i + nx, j + ny) not in pacific_set:
                    pacific_dfs(i + nx, j + ny)


        def atlantic_dfs(i, j):

            curr = heights[i][j]
            atlantic_set.add((i,j))
            
            for nx, ny in [(1,0), (0,1), (0,-1), (-1,0)]:
                if 0 <= i + nx < rows and 0 <= j + ny < cols and heights[i + nx][j + ny] >= curr and (i + nx, j + ny) not in atlantic_set:
                    atlantic_dfs(i + nx, j + ny)

        for j in range(rows):
            pacific_dfs(j, 0)

        for i in range(cols):
            pacific_dfs(0, i)

        for j in range(rows):
            atlantic_dfs(j, cols - 1)

        for i in range(cols):
            atlantic_dfs(rows - 1, i)
            
        total = []
        for (i, j) in pacific_set:
            if (i, j) in atlantic_set:
                total.append([i,j])

        return total
