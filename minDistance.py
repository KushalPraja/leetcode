from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        mapping = {}

        for i in range(len(nums)):
            if nums[i] not in mapping:
                mapping[nums[i]] = []

            mapping[nums[i]].append(i)

        distance = float('inf')
        for i in list(mapping.values()):
            if len(i) >= 3:
                for j in range(len(i) - 2):
                    distance = min(distance, abs(i[j] - i[j + 1]) + abs(i[j] - i[j + 2]) + abs(i[j + 1] - i[j + 2]))
            
        return distance if distance != float('inf') else -1         