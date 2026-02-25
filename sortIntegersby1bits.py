from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        mapd = {}
       
        for i in arr:
            count = 0
            integer = bin(i)
            for j in integer:
                if j == "1":
                    count += 1
            
            if count not in mapd:
                mapd[count] = []
            mapd[count].append(i)
        
        listy = list(mapd.items())
        listy.sort()
        listy = [i for _,sublist in listy for i in sorted(sublist)]
        return listy
