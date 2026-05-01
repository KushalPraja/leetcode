from typing import List


# F(n) = 0 * nums[0] + 1 * nums[1] + ... + (n-1) * nums[n-1]
# F(n-1) = 0 * nums[1] + 1 * nums[2] + ... + (n-2) * nums[n-1] + (n-1) * nums[0]
# F(n-1) = F(n) + sum(nums) - n * nums[n-1]

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:

        
        sum_nums = sum(nums)
        n = len(nums)
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[0] += nums[i] * i

        for i in range(1, len(dp)):
            dp[i] = dp[i-1] + sum_nums - n * nums[n - i] 
        
    
        return max(dp)

