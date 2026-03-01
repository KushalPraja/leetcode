class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])


        def update(r, c):
            temp = copy.deepcopy(board)

            directions = [(1,0), (0,1), (-1, 0), (0, -1)]
            queue = deque([(r,c)])

            touches_border= False
            region = [(r,c)]
            temp[r][c] = "X"

            while queue:
                curr_r, curr_c = queue.popleft()

                if curr_r == 0 or curr_r == ROWS-1 or curr_c == 0 or curr_c == COLS-1:
                    touches_border = True
                
                for x, y in directions:
                    if 0 <= x + curr_r < ROWS and 0 <= y + curr_c < COLS and temp[x + curr_r][y + curr_c] == "O":

                        queue.append((x + curr_r, y + curr_c))
                        region.append((x + curr_r, y + curr_c))
                        temp[x + curr_r][y + curr_c] = "X"


            # update only if not touches boarder
            if not touches_border:
                for rr, cc in region:
                    board[rr][cc] = 'X'
                

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    update(r, c)
