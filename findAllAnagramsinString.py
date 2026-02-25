from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start_indexes = []
        sorted_p = sorted(p)

        for i in range(len(s) - len(p) + 1):
            if sorted(s[i:i + len(p)]) == sorted_p:
                start_indexes.append(i)
        
        return start_indexes
