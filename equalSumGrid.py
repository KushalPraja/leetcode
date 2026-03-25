from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:

        row_sum = [0] * len(grid)
        col_sum = [0]* len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr = grid[i][j]
                row_sum[i] += curr
                col_sum[j] += curr

        prefix_sum = [0] * len(grid)

        for i in range(len(row_sum)):
            prefix_sum[i] += row_sum[i]
            if i > 0:
                prefix_sum[i] += prefix_sum[i - 1] 

        if prefix_sum[-1] % 2 == 0 and prefix_sum[-1] // 2 in prefix_sum:
            return True

        prefix_sum = [0] * len(grid[0])

        for i in range(len(col_sum)):
            prefix_sum[i] += col_sum[i]
            if i > 0:
                prefix_sum[i] += prefix_sum[i - 1] 

        if prefix_sum[-1] % 2 == 0 and prefix_sum[-1] // 2 in prefix_sum:
            return True


        return False