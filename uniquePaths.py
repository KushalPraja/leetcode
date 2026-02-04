class Solution:
    def uniquePaths(self, m: int, n: int) -> int:


        grid = [[0] * n for _ in range(m)]


        grid[0][0] = 0
        for i in range(0, n):
            grid[0][i] = 1

        for i in range(0, m):
            grid[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        

        print(grid)

        return grid[m-1][n-1]
        
