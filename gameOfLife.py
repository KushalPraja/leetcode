from typing import List

class Solution:

    def gameOfLife(self, board: List[List[int]]) -> None:
        original_board = [row[:] for row in board]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (self.checkNeighbours(original_board, i, j)):
                    board[i][j] = 1
                else:
                    board[i][j] = 0

    def checkNeighbours(self, main_board, r, c):
        neighbours = 0
        directions = [(-1, 0), (1,0), (0,1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

        for x, y in directions:
            if 0 <= x + r < len(main_board) and 0 <= y + c < len(main_board[0]) and main_board[x+r][y+c] == 1:
                neighbours += 1
    
        if main_board[r][c] == 1 and 2 <= neighbours <= 3 :
            return True
        
        if main_board[r][c] == 0 and neighbours == 3:
            return True
        
        return False
