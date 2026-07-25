from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        temp = sorted(list(set(arr)))
        hashmap = {}

        for i in range(len(temp)):
            hashmap[temp[i]] =  i + 1

        for j in range(len(arr)):
            arr[j] = hashmap[arr[j]]

        return arr
