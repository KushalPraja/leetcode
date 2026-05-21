from typing import List


# store all possible prefixes and compare
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        x = set()
        for i in range(len(arr1)):
            for j in range(len(str(arr1[i]))):
                x.add(int(str(arr1[i])[0:j + 1]))


        count = 0

        for i in range(len(arr2)):
            for j in range(len(str(arr2[i]))):
                if int(str(arr2[i])[0:j + 1]) in x:
                    count = max(count, len(str(arr2[i])[0:j + 1]))

        return count
