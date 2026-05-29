from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:

        min_element = float('inf')

        for i in nums:
            temp =  0
            for j in str(i):
                temp += int(j)

            min_element = min(min_element, temp)

        return min_element

