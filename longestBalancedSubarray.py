from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        
        max_sub = 0
        for i in range(len(nums)):
            odd_count = 0
            even_count = 0
            temp = set()
            for j in range(i, len(nums)):
                if nums[j] in temp:
                    pass
                elif nums[j] % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1

                temp.add(nums[j])

                if even_count == odd_count:
                    max_sub = max(max_sub, j - i + 1)

        return max_sub
                
