from typing import List

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        new_arr = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] > 0:
                val = (i + nums[i]) % len(nums) 
                val = nums[val]
                new_arr[i] = val

            elif nums[i] < 0:
                val = (i - (abs(nums[i]) % len(nums)))
                val = nums[val]
                new_arr[i] = val

            else:
                new_arr[i] = nums[i]
        
        return new_arr
