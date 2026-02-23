class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        temp = set()
        l = 0
        r = k - 1

        if len(s) < r:
            return False

        while r != len(s):
            temp.add(int(s[l:r+1], 2))
            r += 1
            l += 1
     
        if len(temp) == 2 **k :
            return True
        return False
