from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # cant have cycles
        # bfs with tracking visited states 

        adj = {}

        for i, j in edges:
            if i not in adj:
                adj[i] = []
            if j not in adj:
                adj[j] = []

            adj[i].append(j)
            adj[j].append(i)

        visited = set()

        def dfs(i, parent):
            if i in visited:
                return False
            
            visited.add(i)
            if i not in adj:
                return True

            for j in adj[i]:
                if j == parent:
                    continue 

                if not dfs(j, i):
                    return False
            return True 

        if not dfs(0, -1):
            return False
        
        return len(visited) == n




