
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: TreeNode | None, low: int, high: int) -> TreeNode | None:
        
        def dfs(root):
            if not root:
                return None

            left = dfs(root.left)
            right = dfs(root.right)

            curr = root.val
            root.left = left
            root.right = right

            if low <= root.val <= high:
                return root
            
            if root.val < low:
                return right
            
            if root.val > high:
                return left

        return dfs(root)
