from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        x = {}

        for i in range(len(nums)):
            if nums[i] in x:
                for num in x[nums[i]]:
                    if abs(i - num) <= k:
                        return True
            else: 
                x[nums[i]] = []

            x[nums[i]].append(i)

        return False
