class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        prev = None
        total = 0
        for i in range(len(nums)):
            if i >= 1 and prev >= 1 and nums[i] == 0:
                prev = prev + 1
            elif nums[i] == 0:
                prev = 1
            else:
                prev = 0
            total += prev
      
        return total
