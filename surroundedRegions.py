from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:

        queue = deque([])
        rows = len(board)
        cols = len(board[0])

        for i in range(cols):
            if board[0][i] == "O":
                queue.append((0, i))

            if board[rows - 1][i] == "O":
                queue.append((rows - 1, i))

        for j in range(1, rows - 1):
            if board[j][0] == "O":
                queue.append((j, 0))

            if board[j][cols - 1] == "O":
                queue.append((j, cols - 1))

        while queue:
            i, j = queue.popleft()
            board[i][j] = "T"

            for nx, ny in [(1,0), (0,1), (0,-1), (-1,0)]:
                if 0 <= nx + i < rows and 0 <= ny + j < cols:
                    if board[nx + i][ny + j] == "O" and (nx + i, ny + j) not in queue:
                        queue.append((nx + i, ny + j))


        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
