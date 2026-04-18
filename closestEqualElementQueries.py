from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        final = []
        mapping = {}

        for i in range(len(nums)):
            if nums[i] not in mapping:
                mapping[nums[i]] = []
            mapping[nums[i]].append(i)

        for i in queries:
            pos = i
            val = nums[i]
            n = len(mapping[val])
            if len(mapping[val]) < 2:
                final.append(-1)
                continue
            
            x = self.binarysearch(mapping[val], pos)
            l = mapping[val][(x - 1) % n]
            r = mapping[val][(x + 1) % n]
            l_dis = min(abs(i - l), len(nums) - abs(i - l))
            r_dis = min(abs(i - r), len(nums) - abs(i - r))
            final.append(min(l_dis, r_dis))
        return final
                
    def binarysearch(self, arr, target):
        left = 0
        right = len(arr) - 1

        while (left <= right):
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1