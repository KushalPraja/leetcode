from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        res = []

        def dfs(start, path_sum, path):
            if len(path) == k:
                if path_sum == n:
                    res.append(path[:])
                return

            for i in range(start, 10):
                path.append(i)
                dfs(i + 1, path_sum + i, path)
                path.pop()
        
        dfs(1, 0, [])

        return res
