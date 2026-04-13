from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:

        min_dis = float('inf')

        targets = []

        for i in range(len(nums)):
            if nums[i] == target:
                targets.append(i)

        targets.sort(key = lambda i : abs(start - i))

        return abs(targets[0] - start)
