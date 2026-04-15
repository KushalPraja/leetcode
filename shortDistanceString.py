from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        
        distance = 0

        l = startIndex
        r = startIndex

        if target not in words:
            return -1
        n = len(words)

        while words[l] != target and words[r] != target:
            l = (l - 1) % n
            r = (r + 1) % n
            distance += 1
    
        return distance
           