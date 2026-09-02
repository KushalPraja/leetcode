from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        visited = {}
        def dfs(node):
            if node.val in visited:
                return visited[node.val]

            temp = Node(node.val)
            visited[temp.val] = temp
            
            for i in node.neighbors:
                temp.neighbors.append(dfs(i))

            return temp

        if node:
            return dfs(node)
        else:
            return None