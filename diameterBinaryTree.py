from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0;
        def dfs(root, depth):
            if not root:
                return depth

            nonlocal diameter
            depth_right = dfs(root.right, depth)
            depth_left = dfs(root.left, depth) 


            if root.right or root.left:
                diameter = max(depth_right + depth_left, diameter)
        
            
            return max(depth_right, depth_left) + 1
        
        dfs(root, 0)
        return diameter
