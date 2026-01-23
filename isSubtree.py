# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return False

        def isSameTree(a, b):
            if not a and not b:
                return True

            elif not a or not b:
                return False
        
            if a.val != b.val:
                return False
            
            return isSameTree(a.left, b.left) and isSameTree(a.right, b.right)

        if isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
