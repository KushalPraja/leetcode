from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        l = 0
        map = {}

        for r in range(10, len(s)+1):
            if s[l:r] in map:
                map[s[l:r]] += 1
            else:
                map[s[l:r]] = 1
            l+=1
        
        return [i for i,j in map.items() if j > 1 ]
