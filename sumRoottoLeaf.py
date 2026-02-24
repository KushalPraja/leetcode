
# Definition for a binary tree node.

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        ttl = 0
        def dfs(root, path_string):
            nonlocal ttl
            path_string += str(root.val)

            if not root.left and not root.right:
                ttl += int(path_string)
                return
            
            if root.right:
                dfs(root.right, path_string)
            
            if root.left:
                dfs(root.left, path_string)

        dfs(root, " ")
        return ttl

