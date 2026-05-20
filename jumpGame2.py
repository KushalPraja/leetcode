from typing import List

# this is a O(n^2) solution not really that optimal

class Solution:
    def jump(self, nums: List[int]) -> int:

        dp = [0] * len(nums)
        dp[0] = 1

        for i in range(len(dp)):
            if dp[i] >= 1:
                for j in range(i, min(i + nums[i] + 1, len(dp))):
                    if dp[j] == 0:
                        dp[j]  = dp[i] + 1

        return dp[-1] - 1