class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        mapping = {}
        mapping2 = {}
        
        temp = s.split(" ")

        if len(pattern) != len(temp):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in mapping and temp[i] not in mapping2:
                key = pattern[i]
                mapping[key] = temp[i]
                mapping2[temp[i]] = key

            if pattern[i] in mapping and mapping[pattern[i]] != temp[i]:
                return False
            
            if temp[i] in mapping2 and mapping2[temp[i]] != pattern[i]:
                return False

        return True