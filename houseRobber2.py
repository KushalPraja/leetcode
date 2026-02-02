from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        def robber(nums):
            arr = [0] * (len(nums))

            if len(nums) == 1:
                return nums[0]
            arr[0] = nums[0]
            arr[1] = nums[1]
            if len(nums) == 2:
                return max(nums[0],nums[1])

            for i in range(2, len(arr)):
                arr[i] = max(nums[i] + arr[i-2], arr[i-1])
                
                if arr[i-2] > arr[i-1]:
                    arr[i-1] = arr[i-2]
            return arr[-1]

        return max(robber(nums[1::]), robber(nums[:len(nums)-1:1]))
