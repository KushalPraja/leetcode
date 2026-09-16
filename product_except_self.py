from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        prefix[0] = nums[0]
        suffix[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]
        
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]
        
        temp = [0] * len(nums)
        temp[0] = suffix[1]
        temp[-1] = prefix[-2]

        for i in range(1, len(temp) - 1):
            temp[i] = prefix[i - 1] * suffix [i + 1]
        
        return temp

