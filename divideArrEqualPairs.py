class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        # this is one way
        # nlogn best case
        # nums.sort()

        # if len(nums) % 2 != 0:
        #     return False

        # stack = []
        # for i in nums:
        #     if i in stack:
        #         stack.pop()

        #     elif stack == []:
        #         stack.append(i)
            
        #     else:
        #         return False

        # return True

        # o(n) solution

        freq = {}

        for i in nums:
            if i not in freq:
                freq[i] = 0

            freq[i] += 1
        
        for i in list(freq.values()):
            if i % 2 != 0:
                return False
        
        return True