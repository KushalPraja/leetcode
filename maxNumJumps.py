from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        
        dp = [-1] * len(nums)
        dp[0] = 0

        for i in range(1, len(dp)):
            max_way = -1

            for j in range(i, -1, -1):
                if dp[j] != -1 and abs(nums[j] - nums[i]) <= target:
                    max_way = max(max_way, dp[j] + 1)
                
            dp[i] = max_way

        return dp[-1] if dp[-1] != -1 else -1
