class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        
        m = len(grid)
        n = len(grid[0])
        end = (m - 1, n - 1)

        directions = [(0,1), (1,0)]

        mapping = {}

        def dfs(i, j, balance):
            

            if grid[i][j] == "(":
                balance += 1

            elif grid[i][j] == ")":
                if balance > 0:
                    balance -= 1
                else:
                    return False

            if (i, j, balance) in mapping:
                return mapping[(i, j, balance)]

            
            if (i, j) == end and balance == 0:
                return True

            for nx, ny in directions:
                if 0 <= nx + i < m and 0 <= ny + j < n:
                    if dfs(i + nx, j + ny, balance):
                        mapping[(i,j, balance)] = True
                        return True

            mapping[(i, j, balance)] = False
            
            return False

        return dfs(0,  0, 0)

           
