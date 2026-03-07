from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            statesrow = set()
            statescol = set()
            for j in range(len(board[0])):
                if board[i][j] != "." and board[i][j] in statesrow:
                    return False

                if board[j][i] != "." and board[j][i] in statescol:
                    return False

                statesrow.add(board[i][j])
                statescol.add(board[j][i])

        for i in range(len(board)//3):
            for j in range(len(board)//3):
                states = set()

                for k in range(i*3,i*3+3):
                    for l in range(j*3,j*3+3):
                        if board[k][l] != "." and board[k][l] in states:
                            print("diag")
                            return False
                        states.add(board[k][l])

        return True