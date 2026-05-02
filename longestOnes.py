from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0

        max_len = 0
        while r < len(nums):
            print(r, l)

            if nums[r] == 1:
                r += 1

            elif nums[r] == 0:
                if k > 0:
                    k -= 1
                    r += 1
                else:
                    # ✅ fix: shrink until we free a zero
                    while k == 0:
                        if nums[l] == 0:
                            k += 1
                        l += 1

            # ✅ move this AFTER window is valid
            max_len = max(max_len, r - l)

        return max_len

            

            


            




        
        