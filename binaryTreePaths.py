# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def dfs(root, path_str):
            if not root.right and not root.left:
                path_str += str(root.val)
                paths.append(path_str)
                return

            if root.left:
                dfs(root.left, path_str + str(root.val) + "->")
            
            if root.right:
                dfs(root.right, path_str + str(root.val) + "->")

        dfs(root, "")
        return paths
