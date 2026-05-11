from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        new_arr = []

        for i in nums:
            for j in str(i):
                new_arr.append(int(j))

        
        return new_arr
