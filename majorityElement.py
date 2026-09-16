from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapping = {}
        max_count = (0, 0)

        for i in nums:
            if i not in mapping:
                mapping[i] = 0
                
            mapping[i] += 1
            if (mapping[i] > max_count[1]):
                max_count = (i, mapping[i])

        return max_count[0]
