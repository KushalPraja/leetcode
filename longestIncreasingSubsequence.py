from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(dp)):

            max_way = 1

            for j in range(i, -1, -1):
                if nums[j] < nums[i]:
                    max_way = max(dp[j] + 1, max_way)

            dp[i] = max_way

        return max(dp)

