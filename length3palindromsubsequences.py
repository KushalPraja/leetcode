class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        start = {}
        cnt = 0
        end = {}

        for i in range(len(s)):
            if s[i] not in start:
                start[s[i]] = i
                continue

            if s[i] in start:
                if i > start[s[i]] + 1:
                    end[s[i]] = i
        
        pairs = []

        for i in start.keys():
            if i in start and i in end:
                pairs.append((start[i], end[i]))

        for i, j in pairs:
            cnt += len(set(s[i + 1:j]))

        return cnt



           
