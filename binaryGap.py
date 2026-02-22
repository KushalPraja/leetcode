class Solution:
    def binaryGap(self, n: int) -> int:
        res = bin(n)[2:]

        l = 0
        r = l + 1
        count = 0

        while r != len(res):
            if res[r] == "1":
                count = max(count, abs(r - l))
                l = r

            r += 1

        return count
