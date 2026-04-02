class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        
        ls1 = []
        ls2 = []
        ls3 = []
        ls4 = []

        for i in range(len(s1)):
            if i % 2 == 0:
                ls1.append(s1[i])
                ls2.append(s2[i])
            else:
                ls3.append(s1[i])
                ls4.append(s2[i])

        if not sorted(ls1) == sorted(ls2):
            return False
        
        if not sorted(ls3) == sorted(ls4):
            return False

        return True
