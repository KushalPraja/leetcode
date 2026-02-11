from typing import List

class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        
        l = 0
        r = 0
        freq = {}
        dsum = 0
        minl = float('inf')

        while r != len(nums):

            if nums[r] not in freq:
                freq[nums[r]] = 1
                dsum += nums[r]
            else:
                freq[nums[r]] += 1

            while l <= r and dsum >= k:
                minl = min(minl, r - l + 1)
                temp = nums[l]
                freq[temp] -= 1
                if freq[temp] == 0:
                    dsum -= temp
                    del freq[temp]
                l+=1
            r+=1
        
        if minl == float('inf'):
            return -1
        else:
            return int(minl) 
            
