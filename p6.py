class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        return [self.multiply(idx, nums) for idx,val in enumerate(nums)]

    def multiply(self, idx, listy):
        product = 1;
        for i in range(len(listy)):
            if i != idx:
                product *= listy[i]
        return product


