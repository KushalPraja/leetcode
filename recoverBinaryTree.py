
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        treelist = []
        sets= []
        def dfs(root):
            dfs(root.left) if root.left else None
            treelist.append(root)
            sets.append(root.val)
            dfs(root.right) if root.right else None

        dfs(root)
        sets = sorted(sets)

        for i in range(len(treelist)):
            if treelist[i].val != sets[i]:
                treelist[i].val = sets[i]
