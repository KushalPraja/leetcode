# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        if not root:
            return

        temp = root.right if root.right else None

        if root.left:
            self.flatten(root.left)
            root.right = root.left
            root.left = None
        
            temp_root = root
            while (temp_root.right):
                temp_root = temp_root.right
            
            temp_root.right = temp

        curr = temp
        while (curr):
            if curr.left:
                self.flatten(curr)
            curr= curr.right

