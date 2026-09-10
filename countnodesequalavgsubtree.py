# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0

        def dfs(node):
            nonlocal count

            if not node:
                return (0, 0)
            left = 0
            right = 0
            lc = 0
            rc = 0
            if node.left:
                left, lc = dfs(node.left)

            if node.right:
                right, rc = dfs(node.right) 

            avg = (left + right + node.val) // (lc + rc + 1)
            if avg == node.val:
                count += 1

            return (left + right + node.val , lc + rc + 1)

        dfs(root)
        return count

        
