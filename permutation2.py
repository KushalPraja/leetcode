class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        nums.sort()

        def dfs(path):
            if len(path) == len(nums):
                res.add(tuple(path))
                return

            for i in range(len(nums)):
                if nums[i] == float('inf'):
                    continue

                path.append(nums[i])
                nums[i] = float('inf')
                dfs(path)
                nums[i] = path[-1]
                path.pop()

        dfs([])
        return list(res)
