from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        sm = 0
        def dfs(path, visited):
            nonlocal sm
            x = 0
            for i in range(len(path)):
                x = x ^ path[i]
            sm += x

            for i in range(visited, len(nums)):
                path.append(nums[i])
                dfs(path, i + 1)
                path.pop()
        
        dfs([], 0)

        return sm
