class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # there are two ways to solve this problem
        # 1. generate all permutations of s1 and check if s2 is a permutation of s1 (this is the brute force way)
        # 2. sort s1 and substring of s2 and check if they are equal (this is also the brute force way)

    
        # s1_split = [i for i in s1]
        # permute = []
        # def generatePermutations(path):
        #     nonlocal permute
        #     if len(path) == len(s1):
        #         permute.append("".join(path[:]))
        #         return
            
        #     for char in s1_split:
        #         if char not in path:
        #             path.append(char)
        #             generatePermutations(path)
        #             path.pop()
        
        # generatePermutations([])
        
        for i in range(0, len(s2) - len(s1) + 1):
            substring = s2[i: i + len(s1)]

            print(substring)
            if sorted(substring) == sorted(s1):
                return True
            
        return False
            
