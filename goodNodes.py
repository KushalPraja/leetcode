class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        goodNodes = 0

        def dfs(root, max_val):
            nonlocal goodNodes

            if not root:
                return
            
            if root.val >= max_val:
                goodNodes += 1
            
            max_val = max(max_val, root.val)

            dfs(root.right, max(max_val, root.val))
            dfs(root.left, max(max_val, root.val))

        dfs(root, root.val)
        return goodNodes
