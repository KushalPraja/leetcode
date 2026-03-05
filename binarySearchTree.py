# Definition for a binary tree node.


from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = deque()
        self.dfs(root)
    
    def dfs(self, root):
        if not root:
            return 
        self.dfs(root.left)

        if root.val != None:
            self.stack.append(root.val)

        self.dfs(root.right)

    def next(self) -> int:
        x = self.stack.popleft()
        return x

    def hasNext(self) -> bool:
        if self.stack:
            return True

        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext(
