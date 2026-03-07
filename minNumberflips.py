class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        minFlips = n

        flips1 = 0  # pattern 010101...
        flips2 = 0  # pattern 101010...

        l = 0

        for i in range(len(s)):
            # add right side contribution
            if i % 2 == 0:
                if s[i] != '0':
                    flips1 += 1
                if s[i] != '1':
                    flips2 += 1
            else:
                if s[i] != '1':
                    flips1 += 1
                if s[i] != '0':
                    flips2 += 1

            if i - l + 1 > n:
                if l % 2 == 0:
                    if s[l] != '0':
                        flips1 -= 1
                    if s[l] != '1':
                        flips2 -= 1
                else:
                    if s[l] != '1':
                        flips1 -= 1
                    if s[l] != '0':
                        flips2 -= 1
                l += 1

            if i - l + 1 == n:
                minFlips = min(minFlips, flips1, flips2)

        return minFlips 


