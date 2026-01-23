# Definition for a binary tree node.

from typing import Optional 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        maxDepth = 0

        def dfs(root, depth):
            nonlocal maxDepth
            if not root:
                maxDepth = max(depth, maxDepth)
                return 

            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)
        
        dfs(root, 0)
        return maxDepth
