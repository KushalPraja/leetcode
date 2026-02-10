class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        max_size = 0
        n = len(nums)

        for l in range(n):
            odd_count = 0
            even_count = 0
            sub_array = set()
            
            for r in range(l, n):
                val = nums[r]
                if val not in sub_array:
                    if val % 2 == 0:
                        even_count += 1
                    else:
                        odd_count += 1
                    sub_array.add(val)
                
                if odd_count == even_count:
                    max_size = max(max_size, r - l + 1)
            
        return max_size