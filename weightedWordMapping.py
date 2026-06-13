from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        

        final_str = ""
        
        for i in words:
            weight = 0

            for j in i:
                j.lower()
                weight += weights[ord(j) - ord('a')]

            weight %= 26
            final_str += chr(ord('z') - weight)


        return final_str