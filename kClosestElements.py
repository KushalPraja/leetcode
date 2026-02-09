from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        arr.sort(key= lambda i: abs(i-x))
        return sorted(arr[:k])
