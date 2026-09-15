from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        last_seen_value = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[last_seen_value] = nums[i]
                last_seen_value += 1

        return last_seen_value
