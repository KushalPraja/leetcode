from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(path):
            if sum(path) >= target:
                if sum(path) == target and sorted(path) not in res:
                    res.append(sorted(path)[:])
                return
            
            for i in range(len(nums)):
                path.append(nums[i])
                dfs(path)
                path.pop()
        

        dfs([])
        return res
