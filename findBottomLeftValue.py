class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        
        levels = []

        def dfs(i, depth):
            if len(levels) < depth:
                levels.append(i.val)
            if i.left:
                dfs(i.left, depth + 1)
            if i.right:
                dfs(i.right, depth + 1)
        

        dfs(root, 1)
        return levels[-1]
