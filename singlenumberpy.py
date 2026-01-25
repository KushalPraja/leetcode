class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        
        x = {}
        for i in nums:
            if i in x:
                x[i] += 1
            else:
                x[i] = 1

        for i in x.items():
            if i[1] == 1:
                return i[0]

        return -1
