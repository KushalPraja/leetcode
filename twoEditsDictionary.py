from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        
        res = []

        for i in range(len(queries)):

            curr = queries[i]

            for j in dictionary:
                diff = 0

                for i in range(len(curr)):
                    if curr[i] != j[i]:
                        diff += 1

                if diff > 2:
                    continue
                
                else:
                    res.append(curr)
                    break
        
        return res