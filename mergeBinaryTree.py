
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(p, q):
            if not p and not q:
                return None

            ttl = 0

            if p:
                ttl += p.val

            if q:
                ttl += q.val

            tree = TreeNode(ttl)
            left_p = p.left if p else None
            left_q = q.left if q else None
            right_p = p.right if p else None
            right_q = q.right if q else None
            tree.left = dfs(left_p, left_q)
            tree.right = dfs(right_q, right_p)
            return tree

        return dfs(root1, root2)