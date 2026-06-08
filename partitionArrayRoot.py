from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        
        leftside = []
        mid = []
        rightside = []


        for i in nums:
            if i < pivot:
                leftside.append(i)

            if i > pivot:
                rightside.append(i)
            
            if i == pivot:
                mid.append(i)

        return leftside + mid + rightside
                