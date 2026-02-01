from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        left = 0 
        right = k
         
        x = []
        max_val = max(nums[left:right])
        while right != len(nums) + 1:
            max_val = max(max_val, nums[right-1])
            x.append(max_val)
            left += 1
            right += 1

        return x
