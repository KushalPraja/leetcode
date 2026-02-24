from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        visited = {}

        def dfs(s, wordDict):
            temp = ""
            if s == "":
                return True
            
            if s in visited:
                return visited[s]

            state = False
            for idx, i in enumerate(s):
                temp += i
                if temp in wordDict:
                    if dfs(s[idx + 1:], wordDict):
                        state = True

            visited[s] = state
            return state

        return dfs(s, wordDict)
