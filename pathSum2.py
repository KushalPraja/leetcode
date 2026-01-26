# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        x = []

        def dfs(root, path):
            nonlocal x

            if root.right:
                path.append(root.val)
                dfs(root.right, path)
                path.pop()
    
            if root.left:
                path.append(root.val)
                dfs(root.left, path)
                path.pop()
            
            if not root.left and not root.right:
                path.append(root.val)
                if sum(path) == targetSum:
                    x.append(path[:])
                path.pop()
                return
        if root:
            dfs(root, [])
        return x;
