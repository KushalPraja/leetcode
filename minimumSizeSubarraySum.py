from typing import List

# simple sliding window approach
# shrink the window as long as sum of elements in window is greater than target
# else expand the window towards the right
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        r = 0
        total = 0
        min_len = float('inf')
        while (r != len(nums)):
            total += nums[r]
            while l<= r and total >= target:
                min_len = min(r - l + 1, min_len)
                total -= nums[l]
                l += 1
            r += 1

        if min_len == float('inf'):
            return 0
        else:
         return int(min_len)

