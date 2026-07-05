class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        

        directions = [(0,-1), (-1,0), (-1,-1)]
        visited = {}

        def dfs(i, j):

            if (i,j) in visited:
                return visited[(i,j)]

            if i == 0 and j == 0:
                return [0,1]

            max_path = float('-inf')
            paths = 0
            curr = int(board[i][j]) if board[i][j] != "S" else 0

            for nx, ny in directions:
                if 0 <= nx + i < len(board) and 0 <= ny + j < len(board[0]) and board[nx + i][ny + j] != "X":
                    score, cnt = dfs(nx + i, ny + j)

                    if score == float("-inf"):
                        continue

                    score += curr

                    if score > max_path:
                        max_path = score 
                        paths = cnt

                    elif score == max_path:
                        paths += cnt

            paths %= (10**9 + 7)
            
            if max_path == float('-inf'):
                visited[(i, j)] = [float('-inf'), 0]
                return [float('-inf'),0]

            visited[(i,j)] = [max_path,paths]

            return [max_path, paths]
                


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "S":
                    return dfs(i, j) if dfs(i, j) != [float('-inf'),0] else [0,0]

        return [0,0]