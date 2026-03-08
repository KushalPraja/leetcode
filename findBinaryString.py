from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        n = len(nums[0])
        def dfs(path):
            if len(path) == n:
                if path not in nums:
                    return path 
                return False

            for i in "01":
                x = dfs(path + i)
                if x:
                    return x
        return dfs("")