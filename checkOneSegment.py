class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        
        found = False
        for i in range(len(s)):
            if s[i] == "1" and found == False:
                found = True
            
            elif found and i >= 1 and s[i] == "1" and s[i - 1] == "0":
                return False

        return True
