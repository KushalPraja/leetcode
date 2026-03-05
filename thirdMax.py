from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        max1 = float('-inf')
        max2 = float('-inf')
        max3 = float('-inf')

        nums = set(nums)

        for i in nums:
            if i > max1:
                temp = max2
                max2 = max1
                max3 = temp
                max1 = i

            elif i > max2:
                max3 = max2
                max2 = i
            
            elif i > max3:
                max3 = i

        if max3 == float('-inf'):
            return max1 
        return max3

