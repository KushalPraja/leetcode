from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        

            A_temp= {}
            B_temp = {}
            result = []

            for i in range(len(A)):
                common = 0
                
                if i >= 1:
                    common = result[-1]
                
                if A[i] == B[i]:
                    common += 1

                if A[i] in B_temp:
                    common += 1

                if B[i] in A_temp:
                    common += 1

                A_temp[A[i]] = 1
                B_temp[B[i]] = 1
                result.append(common)
            
            return result

            


