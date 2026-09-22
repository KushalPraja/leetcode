class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        
        # approach backtacking 
        # len 
        # return if len
        # do a visited array
        # do not go back in array
        # if no valid path 
        # return 

        rows = len(grid)
        cols = len(grid[0])
        len_path = 0
        starting = (0, 0)
        ending = (0, 0)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != -1:
                    len_path += 1
                if grid[i][j] == 1:
                    starting = (i, j)
                if grid[i][j] == 2:
                    ending = (i, j)

        count = 0
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        
        def dfs(i, j, visited):

            visited.add((i,j))
            
            nonlocal count
            if (i, j) == ending:
                if len(visited) == len_path:
                    count += 1
                visited.remove((i,j))
                return

            for nx, ny in directions:
                if 0 <= nx + i < rows and 0 <= ny + j < cols:
                    if (nx+i, ny + j) not in visited:
                        if grid[nx + i][ny + j] != -1:
                            dfs(nx + i, ny + j, visited)

            visited.remove((i,j))
            return

        dfs(starting[0], starting[1], set())
        return count

       
