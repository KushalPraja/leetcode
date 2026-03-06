from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        def dfs(start, path):
            if len(path) == k:
                res.append(path[:])

            for i in range(start, n + 1):
                path.append(i)
                dfs(i+1, path)
                path.pop()

        dfs(1, [])
        return res
