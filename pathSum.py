# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        found = False

        def dfs(root, pathVal):
            nonlocal found
            if root.left:
                dfs(root.left, pathVal + root.val)

            if root.right:
                dfs(root.right, pathVal + root.val)

            if not root.right and not root.left:
                if (pathVal + root.val == targetSum):
                    found = True

            return
        
        if root:
            dfs(root, 0)

        if found:
            return True
        return False

