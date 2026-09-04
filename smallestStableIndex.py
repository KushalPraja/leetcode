class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        max_nums = [0] * len(nums)
        min_nums = [0] * len(nums)
        max_so_far = 0
        min_so_far = float('inf')

        for i in range(len(nums)):
            if nums[i] > max_so_far:
                max_so_far = nums[i]
            max_nums[i] = max_so_far


        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < min_so_far:
                min_so_far = nums[i]
            min_nums[i] = min_so_far
        
        for i in range(len(nums)):
            if max_nums[i] - min_nums[i] <= k:
                return i
        
        return -1
