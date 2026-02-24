
# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        sum_x = 0

        def dfs(root, path_sum):
            nonlocal sum_x
            path_sum += str(root.val)
            
            if root.left:
                dfs(root.left, path_sum)
            if root.right:
                dfs(root.right, path_sum)  

            if not root.right and not root.left:
                sum_x += int(path_sum, 2)
                return

        dfs(root, "")
        return sum_x
