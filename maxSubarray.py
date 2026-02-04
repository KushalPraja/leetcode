from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
     
        new_array= [0] * len(nums)
        new_array[0] = nums[0]

        for i in range(1, len(nums)):
            new_array[i] = max(nums[i], new_array[i-1] + nums[i])

        return max(new_array)

       
