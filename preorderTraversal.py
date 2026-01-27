from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        x = []
        def dfs(root):
            nonlocal x

            if not root:
                return 
        
            x.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return x

