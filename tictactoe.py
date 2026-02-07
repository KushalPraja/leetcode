class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        

        grid = [[0] * 3 for _ in range(3)] 

        curr = "A"
        for i,j in moves:
            grid[i][j] = curr
            curr = "A" if curr == "B" else "B"
 
        for i in range(len(grid)):
            if grid[i][0] == grid[i][1] == grid[i][2] != 0:
                return grid[i][0]
            if grid[0][i] == grid[1][i] == grid[2][i] != 0:
                return grid[0][i]
            
        if grid[0][0] == grid[1][1] == grid[2][2] != 0:
            return grid[0][0]

        if grid[0][2] == grid[1][1] == grid[2][0] != 0:
            return grid[0][2]
        
        if len(moves) == 9:
            return "Draw"
        
        return "Pending"