from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            largest = nums1
            smallest = nums2
        else:
            largest = nums2
            smallest = nums1

        mapping = {}
        for i in largest:
            if i not in mapping:
                mapping[i] = 0
            mapping[i] += 1

        final_arr = []
        for i in smallest:
            if i in mapping and mapping[i] > 0:
                final_arr.append(i)
                mapping[i] -= 1
            
        return final_arr
