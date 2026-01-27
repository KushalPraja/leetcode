from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(start, path):
            if sorted(path) not in res:
                res.append(sorted(path)[:])

            if len(path) == len(nums):
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()

        dfs(0, [])
        return res

if __name__ == "__main__":
    print(Solution().subsetsWithDup([1,2,1]))