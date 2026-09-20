class Solution:
    def reverseDegree(self, s: str) -> int:
        
        ttl = 0
        for i in range(len(s)):
            curr_char = s[i]
            ttl +=  (ord('{') - ord(curr_char)) * (i + 1) 

        return ttl
