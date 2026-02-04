from typing import List

# O(N) shit solution i fking hate this problem
# lost braincells on ts

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        l = 0
        r = len(nums) - 1

        if len(nums) <= 3:
            return False

        while l < len(nums) - 1 and nums[l] < nums[l+1]:
            if nums[l] >= nums[l+1]:
                break
            l += 1
        
        while r >= 0 and nums[r] > nums[r-1]:
            if nums[r-1] > nums[r]:
                break
            r -= 1

        for i in range(l, r):
            if nums[i] <= nums[i+1]:
                return False
        
        if l < r and l > 0 and r < len(nums) - 1:
            return True

        return False
