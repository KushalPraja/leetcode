
from typing import List


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:


        for i in boxGrid:
            corner = len(i)
            l = len(i) - 1
            
            while l >= 0:
                moves = 0
                if i[l] == "#":
                    while l + moves + 1 < corner:
                        moves += 1
                    i[l], i[l + moves] = i[l + moves], i[l]
                    corner = l + moves
                
                if i[l] == "*":
                    corner = l

                l -= 1

        m = len(boxGrid)
        n = len(boxGrid[0])

        new_grid = [[0] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                new_grid[j][m - i - 1] = boxGrid[i][j]

        return new_grid