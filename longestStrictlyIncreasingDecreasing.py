class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        increasing = [1] * len(nums)
        decreasing = [1] * len(nums)
        

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increasing[i]= increasing[i-1] + 1
            
            if nums[i] < nums[i - 1]:
                decreasing[i]= decreasing[i-1] + 1

        
        return max(max(increasing), max(decreasing))
            
