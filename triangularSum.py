class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        else:
            new_nums = [0] * (len(nums)-1)
            for i in range(len(nums)-1):
                new_nums[i] = (nums[i] + nums[i + 1]) % 10
            return self.triangularSum(new_nums)

