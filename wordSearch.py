from typing import List, Optional

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(visited, curr, i, j):
            if curr == len(word) - 1:
                return True
            visited.append((i,j))
            directions = [(1,0), (0,1), (0,-1), (-1,0)]
            for dx, dy in directions:
                if (i + dx, j + dy) not in visited and 0 <= i + dx < len(board) and 0 <= j + dy < len(board[0]) and board[i + dx][j + dy] == word[curr + 1]:            
                    if dfs(visited, curr + 1, i + dx, j + dy):
                        return True
            visited.pop()
            return False
    
        word = list(word)
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs([], 0, i, j):
                    return True
        
        return False
       