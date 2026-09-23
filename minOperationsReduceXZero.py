
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
       
        prefix_sum = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                prefix_sum[i] = nums[i]
                continue
            
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        goal = sum(nums) - x
        mapping = {
            0: -1
        }
        min_goal = -1
    
        for i in range(len(nums)):

            curr = prefix_sum[i]
            diff = curr - goal

            if curr not in mapping:
                mapping[curr] = i

            if diff in mapping:
                min_goal = max(min_goal, i - mapping[diff])
            
        if (min_goal == -1):
            return -1
        return len(nums) - min_goal



