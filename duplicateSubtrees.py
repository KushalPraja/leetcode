class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode | None) -> list[TreeNode | None]:
        

        temp = {}
        res = []    

        def dfs(root):
            if not root:
                return "."

            left = dfs(root.left)
            right = dfs(root.right)
            curr = f"{root.val}({left})({right})"

            if curr not in temp:
                temp[curr] = 1
            else:
                temp[curr] += 1
                if temp[curr] == 2:
                    res.append(root)

            return curr

        
        dfs(root)
        return res


