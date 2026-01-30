# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('inf'), float('-inf'))

    def dfs(self, root, upper, lower):
        if not lower < root.val < upper:
            return False
        
        left =  self.dfs(root.left, root.val, lower) if root.left else True
        right =   self.dfs(root.right, upper, root.val) if root.right else True

        return right and left
