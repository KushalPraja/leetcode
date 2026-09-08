class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        nodes = list(range(n + 1))
        ranks = [0] * (n + 1)

        def find(node):
            if nodes[node] != node:
                nodes[node] = find(nodes[node])
            return nodes[node]

        def union(x, y):
            find_x, find_y = find(x), find(y)

            if find_x == find_y:
                return False
            
            if ranks[find_x] > ranks[find_y]:
                find_x,find_y = find_y, find_x

            nodes[find_y] = find_x

            if ranks[find_x] == ranks[find_y]:
                ranks[find_x] += 1
            
            return True

        for i, j in edges:
            if not union(i, j):
                return [i,j]
        
        return []

        

