from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        directions = [(1,0), (0,1)]
        visited = {}
        def dfs(ignores, i, j):
            if i == len(coins) - 1 and j == len(coins[0]) - 1:
                if coins[i][j] < 0:
                    if ignores:
                        return 0
                return coins[i][j]

            if (i, j, ignores) in visited:
                return visited[(i,j,ignores)]

            min_path = float('-inf')
            for x, y in directions:
                if 0 <= x + i < len(coins) and 0<= y + j < len(coins[0]):
                    min_path = max(min_path, coins[i][j] + dfs(ignores, i + x, y + j))
                    if ignores > 0 and coins[i][j] < 0:
                        min_path = max(min_path, dfs(ignores - 1, i + x, y + j))
            
            visited[(i,j,ignores)] = min_path
            return min_path

        return dfs(2, 0, 0)