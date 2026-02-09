from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        levels = {}

        def dfs(level, root):
            if not root:
                return 

            if level in levels:
                levels[level] = max(root.val, levels[level])
            else:
                levels[level] = root.val

            dfs(level + 1, root.right)
            dfs(level + 1, root.left)

        dfs(0, root)
        return list(levels.values())
