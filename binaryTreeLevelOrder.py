# Definition for a binary tree node.

from typing import List, Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        levels = {};
        
        def dfs(level, root):
            nonlocal levels
            if not root:
                return

            if level not in levels:
                levels[level] = [];

            levels[level].append(root.val)


            dfs(level + 1, root.left)
            dfs(level + 1, root.right)
            return

        dfs(0, root);
        return list(levels.values())



