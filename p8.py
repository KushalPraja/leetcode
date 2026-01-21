class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = sorted(list(set(nums)))
        if not nums:
            return 0
        start = 0
        end = 0
        max_size = float('-inf')
        while(end != len(nums) - 1):
            if nums[end] + 1 == nums[end + 1]:
                end += 1
            else:
                max_size = max(end-start+1, max_size)
                start = end + 1
                end += 1

        max_size = max(end-start+1, max_size)
        return int(max_size)

x = Solution().longestConsecutive([1,2,3,4,5,6,7,8])
print(x)

