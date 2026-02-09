class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0 
        l = 0
        r = 0
        temp = 1
        
        while (r < len(nums)):
            if temp * nums[r] < k:
                count += r - l + 1
                temp *= nums[r]
                r += 1
            
            elif l < r:
                temp /= nums[l] 
                l += 1
            
            else:
                r += 1
                l = r
             
        return count

