from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        mem = {}
        
        def dfs(curr: str) -> List[int]:
            if curr in mem:
                return mem[curr]

            if curr.isdigit():
                return [int(curr)]

            ls = []
            for i in range(len(curr)):
                if curr[i] in {"+", "-", "*"}:
                    left = dfs(curr[:i])
                    right = dfs(curr[i+1:])
                    for l in left:
                        for r in right:
                            if curr[i] == '+':
                                ls.append(l + r)
                            elif curr[i] == '-':
                                ls.append(l - r)
                            elif curr[i] == '*':
                                ls.append(l * r)
                        
            mem[curr] = ls
            return ls

        return dfs(expression)
