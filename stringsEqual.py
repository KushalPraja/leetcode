class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                for j in range(i,len(s1)):
                    if s1[j] == s2[i] and j - i == 2:
                        s1[i], s1[j] = s1[j], s1[i]
        return s1 == s2
