from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = n
        cols = 10


        mapping = set()
        for i in reservedSeats:
            mapping.add((i[0], i[1]))
        
        temp = {}

        for i, j in mapping:
            if i not in temp:
                temp[i] = [True, True, True]
            
            if 2 <= j <= 3:
                temp[i][0] = False
            
            if 4 <= j <= 5:
                temp[i][0] = False
                temp[i][1] = False

            if 6 <= j <= 7:
                temp[i][1] = False
                temp[i][2] = False

            if 8 <= j <= 9:
                temp[i][2] = False

        ttl = 0
        for i, j, k in temp.values():
            if i and k:
                ttl += 2
            elif i or j or k:
                ttl += 1


        x = len(temp)
        ttl += (n - x) * 2

        return ttl

             
