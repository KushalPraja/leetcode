# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
         

        def dfs(root):

            if not root:
                return [0, 0]

            left = dfs(root.left)
            right = dfs(root.right)
           
            left_far = left[1] 
            right_far = right[1] 

            rob = left_far + right_far + root.val
            skip = max(left) + max(right)

            return [rob, skip]

        return max(dfs(root))