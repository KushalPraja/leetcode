from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
       
        max_num = max(nums)
        nums.sort()

        if len(nums) != max_num + 1:
            return False
        
        for i in range(1, len(nums)):
            if i != nums[i - 1]:
                return False

        return True
    
    
