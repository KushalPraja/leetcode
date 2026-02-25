from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list1 = set(nums1)
        list2 = set(nums2)

        x = []

        for i in list1:
            if i in list2:
                x.append(i)

        return x
