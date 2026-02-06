from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        max_keep = 1
        right = 0

        while right != len(nums):
            if nums[left] * k >= nums[right]:
                right += 1
            
            else:
                while nums[left] * k < nums[right]:
                    left += 1
            
            max_keep = max(max_keep, (right - left))
            
        return len(nums) - max_keep
