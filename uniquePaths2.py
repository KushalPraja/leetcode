from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        visited = {}
        def directions(r, c):
            if r == len(obstacleGrid) - 1 and c == len(obstacleGrid[0]) - 1:
                if obstacleGrid[r][c] == 1:
                    return 0
                return 1

            elif (r, c) in visited:
                return visited[(r,c)]

            ways = 0
            for x, y in [[1,0],[0, 1]]:
                if 0 <= x + r < len(obstacleGrid) and 0 <= y + c < len(obstacleGrid[0]) and obstacleGrid[x + r][y + c] != 1:
                    ways += directions(x+r, y+c)
            
            visited[(r,c)] = ways
            return ways
        
        return directions(0, 0) if obstacleGrid[0][0] == 0 else 0

            

