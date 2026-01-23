from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, depth):
            if not root:
                return depth
            
            depth_r = dfs(root.right, depth)
            if (depth_r == -1):
                return -1;

            depth_l = dfs(root.left, depth)

            if (depth_l == -1):
                return -1;

            if (abs(depth_r - depth_l)>1):
                return -1;

            return 1 + max(depth_l, depth_r)
        if (dfs(root, 0) != -1):
            return True
        
        return False
