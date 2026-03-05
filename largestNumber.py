from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
    
        for i in range(1, len(nums)):
            idx = i
            while idx > 0 and int(str(nums[idx]) + str(nums[idx-1])) >  int(str(nums[idx - 1]) + str(nums[idx])):
                    nums[idx], nums[idx-1] = nums[idx-1], nums[idx]
                    idx -= 1

        x = "".join([str(i) for i in nums])
        if int(x) == 0:
            return "0"
        else:
            return x
