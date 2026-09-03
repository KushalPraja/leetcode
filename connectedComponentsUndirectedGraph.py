from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        islands = 0

        adj = {}
        visited = set()

        for i,j in edges:
            if i not in adj:
                adj[i] = []
            
            if j not in adj:
                adj[j] = []

            adj[i].append(j)
            adj[j].append(i)

        def dfs(i, parent):
            visited.add(i)
            if i not in adj:
                return 
            
            for j in adj[i]:
                if j == parent:
                    continue
                if j in visited:
                    continue
                dfs(j, i)

        
        for i in range(n):
            if i in visited:
                continue
            dfs(i, -1)
            islands += 1

        return islands