class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        mapping = {}
        for i in arr:
            if i in mapping:
                mapping[i] +=1
            else:
                mapping[i] = 1

        stds = list(mapping.items())
        stds = sorted(stds, key = lambda item : item[1])

        amount = k
        cap = len(stds)

        for i in stds:
            amount = amount - i[1]
            if amount >= 0:
                cap -= 1
            else:
                break
        
        return cap