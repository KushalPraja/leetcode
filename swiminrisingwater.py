class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        directions = [(1,0), (0,1), (0, -1), (-1, 0)]
        que = [(grid[0][0], 0, 0)]
        cnt = grid[0][0]
        visited = {(0, 0)}
        
        while que:
            cnt += 1
            curr_cost, curr_x, curr_y = heapq.heappop(que)

            if curr_x == rows - 1 and curr_y == cols - 1:
                return curr_cost
            
            for nx, ny in directions:
                if 0 <= nx + curr_x < rows and 0 <= ny + curr_y < cols and (nx + curr_x, ny + curr_y) not in visited:
                    new_cost = max(curr_cost, grid[nx + curr_x][ny + curr_y])
                    heapq.heappush(que, (new_cost, nx + curr_x, ny + curr_y))
                    visited.add((nx + curr_x, ny + curr_y))
        
        return -1
