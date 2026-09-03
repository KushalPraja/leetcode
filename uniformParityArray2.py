class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:

        even = []
        odd = []

        for i in nums1:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        if len(even) == len(nums1):
            return True

        minOdd = min(odd)
        for i in nums1:
            if i % 2 == 0:
                if minOdd <= i - 1:
                    continue
                else:
                    return False
                        
        return True