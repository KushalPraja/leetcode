# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def storeInorder(self, root, path):
        if not root:
            return

        self.storeInorder(root.left, path)
        path.append(root.val)
        self.storeInorder(root.right, path)

    def constructBST(self, path, lower, upper):
        if lower > upper:
            return None
        
        mid = (lower + upper) // 2
        root = TreeNode(path[mid])
        root.left = self.constructBST(path, lower, mid - 1)
        root.right = self.constructBST(path, mid + 1, upper)
        return root

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        x = []
        self.storeInorder(root, x)
        return self.constructBST(x, 0, len(x) - 1)
         

