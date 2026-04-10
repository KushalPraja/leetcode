from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:

        distance = float('inf')

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):

                    if nums[i] == nums[j] == nums[k]:
                        distance = min(distance, abs(i - j) + abs(j - k) + abs(k - i))

        
        if distance == float('inf'):
            return -1

        return distance