from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    dfs(path)
                    path.pop()
        
        dfs([])
        return res

if __name__ == "__main__":
    x = [1,2,3]
    y = Solution().permute(x)
    print(y)