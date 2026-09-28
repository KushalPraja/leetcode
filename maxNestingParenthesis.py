class Solution:
    def maxDepth(self, s: str) -> int:
        
        maxDepth = 0

        currDepth = 0
        for i in s:
            if i == "(":
                currDepth += 1
                maxDepth = max(maxDepth, currDepth)

            if i == ")":
                currDepth -=1

        return maxDepth
           
