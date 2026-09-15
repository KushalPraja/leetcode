from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        l = 0
        r = 0

        while (r != len(min(strs))):
            temp = strs[0][r]
            for i in strs:
                if i[r] != temp:
                    return strs[0][l:r]
            r += 1

        return strs[0][l:r]


