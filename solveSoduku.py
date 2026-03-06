from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = {}
        cols = {}
        diags = {}

        for i in range(9):
            for j in range(9):
                if i not in rows:
                    rows[i] = set()

                if j not in cols:
                    cols[j] = set()

                diag = i // 3 * 3 + j // 3

                if diag not in diags:
                    diags[diag] = set()
                
                curr = board[i][j]

                if curr != ".":

                    cols[j].add(curr)
                    rows[i].add(curr)
                    diags[diag].add(curr)

        return self.dfs(board, 0, 0, rows, cols, diags)

    def dfs(self, board, row, col, rows, cols, diags):

        if row == len(board):
            return True

        if col + 1 < len(board[0]):
            next_row, next_col = row, col + 1

        else:
            next_row, next_col = row + 1, 0

        # skip if alr filld
        if board[row][col] != ".":
            return self.dfs(board, next_row, next_col, rows, cols, diags)

        diag = (row // 3) * 3 + col // 3

        for idx in range(1, 10):
            i = str(idx)
            if i in rows[row] or i in cols[col] or i in diags[diag]:
                continue

            board[row][col] = i
            rows[row].add(i)
            cols[col].add(i)
            diags[diag].add(i)

            if self.dfs(board, next_row, next_col, rows, cols, diags):
                return True

            board[row][col] = "."
            rows[row].remove(i)
            cols[col].remove(i)
            diags[diag].remove(i)

        return False
