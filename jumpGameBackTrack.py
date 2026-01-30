from typing import List

# note that this is a brute force solution and not efficient
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        def jumps(current_idx):
            if current_idx >= len(nums) - 1:
                return True

            current_jumps = nums[current_idx]

            for i in range(1, current_jumps+1):
                if jumps(current_idx + i):
                    return True
            
            return False
        return jumps(0)
