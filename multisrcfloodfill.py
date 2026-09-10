class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:

        queue = deque([])
        board = [[0] * m for _ in range(n)]
        sources.sort(key = lambda i:i[2] * -1)

        for temp in sources:
            x = temp[0]
            y = temp[1]
            color = temp[2]
            board[x][y] = color
            queue.append((x,y))

        while queue:
            x, y =  queue.popleft()
            color = board[x][y]

            for nx, ny in [(1,0), (0,1), (-1, 0), (0, -1)]:
                if 0 <= nx + x < n and 0 <= ny + y < m:
                    if board[nx + x][ny + y] == 0:
                        board[nx + x][ny + y] = color
                        queue.append((nx + x, ny + y))

        return board
