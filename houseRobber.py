from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        listx = [0]*len(nums)

        listx[0] = nums[0]
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])
        listx[1]  = nums[1]

        for i in range(2, len(nums)):

            if listx[i - 1] > nums[i] + listx[i-2]:
                listx[i] = listx[i -1]
            
            else:
                listx[i] = nums[i] + listx[i - 2]

            if listx[i - 2] > listx[ i - 1]:
                listx[i - 1]  = listx[i - 2]
      
        return listx[-1]

