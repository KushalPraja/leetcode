class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS = len(board)
        COLUMNS = len(board[0])
        for x in range(ROWS):
            for y in range(COLUMNS):
                if (board[x][y] == word[0]):
                    if (self.dfs(board, list(word),[(x,y)])):
                        return True
        return False

    def dfs(self, board, string, visited):
        string.pop(0)
        if not string:
            return True
        DIRECTIONS = [(1,0),(-1,0),(0,-1),(0,1)]
        ROWS = len(board)
        COLS = len(board[0])
        for (i,j) in DIRECTIONS:
            x = visited[0][1]
            y = visited[0][0]
            if 0<=x+i<COLS and 0<=y+j<ROWS:
                if board[y+j][x+i] == string[0] and (y+j,x+i) not in visited:
                    visited.insert(0,(y+j, x+i))
                    if self.dfs(board, string[:], visited): return True
                    visited.pop(0)
       
        return False
            
