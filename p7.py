class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(len(board)): # rows
            list_rows = []
            list_cols = []
            for j in range(len(board[0])): #columns
                if board[i][j] in list_rows:
                    return False 
                if board[j][i] in list_cols:
                    return False
                if board[i][j] != ".":
                    list_rows.append(board[i][j])
                if board[j][i] != ".":
                    list_cols.append(board[j][i])
        for i in range(3):
            for j in range(3):
                list_diag = []
                starting_i = i * 3 
                starting_j = j * 3

                for l in range(starting_i, starting_i + 3):
                    for m in range(starting_j, starting_j + 3):
                        if board[l][m] in list_diag:
                            return False
                        if board[l][m] != ".":
                            list_diag.append(board[l][m])
        return True
