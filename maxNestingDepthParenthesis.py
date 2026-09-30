class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:

        ans = []
        depth = 0

        for i in range(len(seq)):

            if seq[i] == "(":
                depth += 1

            if depth % 2 == 0:
                ans.append(1)
            else:
                ans.append(0)

            if seq[i] == ")":
                depth -= 1
                
        return ans
