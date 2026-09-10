class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        rows = len(board)
        cols = len(board[0])
        temp = deque([])

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "M":
                    temp.append((i,j))

        mapping = {}

        directions = [(0,1), (1,0), (-1, 0), (0,-1), (-1,1), (1,1), (1, -1), (-1, -1)]
        while temp:
            i, j = temp.popleft()

            for nx, ny in directions:
                if 0 <= i + nx < rows and  0 <= j + ny < cols:
                    if (i + nx, j + ny) not in mapping:
                        mapping[(i + nx, j + ny)] = 0
                    mapping[(i + nx, j + ny)] += 1

        def dfs(i, j):
            if board[i][j] == "M":
                board[i][j] = "X"
                return

            if (i, j) in mapping:
                board[i][j] = str(mapping[(i, j)])
                return

            if (i, j) not in mapping:
                board[i][j] = "B"
                for nx, ny in directions:
                    if 0 <= i + nx < rows and 0 <= j + ny < cols and board[i + nx][j + ny] == "E":
                        dfs(i + nx, j + ny)
        
        dfs(click[0], click[1])
        return boar
