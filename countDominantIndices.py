from typing import List

class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        dominant = 0

        for i in range(len(nums)):
            if nums[i] > sum(nums[i:len(nums)])/(len(nums)-i):
                dominant += 1
        
        return dominant
            
