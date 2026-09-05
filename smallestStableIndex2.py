

from typing import List

class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        
        mx = []

        max_so_far = 0
        for i in range(len(nums)):
            if nums[i] > max_so_far:
                max_so_far = nums[i]
            
            mx.append(max_so_far)

        mn = [0] * len(nums)

        min_so_far = float('inf')

        for i in range(len(nums) - 1, - 1, -1):
            if nums[i] < min_so_far:
                min_so_far =  nums[i]

            mn[i] = min_so_far

        for i in range(len(nums)):
            temp = mx[i] - mn[i]
            if temp <= k:
                return i
        
        return -1