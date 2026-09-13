
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        queue = deque([(root, 1)])
        temp = 1

        while queue:
            curr, cnt = queue.popleft()
            if cnt != temp:
                return False
            temp += 1
            if curr.left:
                left = curr.left
                queue.append((left, cnt * 2))

            if curr.right:
                right = curr.right
                queue.append((right, cnt * 2 + 1))

        return True


