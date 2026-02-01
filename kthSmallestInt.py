# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        queue = []

        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            queue.append(root.val)
            dfs(root.right)

        dfs(root)
        return queue[k-1]

