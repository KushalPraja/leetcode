from typing import Optional

class Node:
    def __init__(self, val: int = 0, left = None, right = None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        levels = {}

        def dfs(root, level):
            nonlocal levels
            if not root:
                return
                        
            if level not in levels:
                levels[level] = root
                root.next = None

            elif level in levels:
                root.next = levels[level]
                levels[level] = root
            
            dfs(root.right, level + 1)
            dfs(root.left, level + 1)
        
        dfs(root, 0)
        return root
                
        
