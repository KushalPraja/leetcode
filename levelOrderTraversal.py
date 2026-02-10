from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = []

        q.append(root)
        curr_level = 0

        while q:
            len_q = len(q)
            res.append([])

            for _ in range(len_q):
                node = q.pop(0)
                res[curr_level].append(node.val)

                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

            curr_level += 1

        return res

