from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
  
        if n == 0:
            return []

        def dfs(lowest, highest) -> List[Optional[TreeNode]]:

            if highest < lowest:
                return [None]
            
            tn_list = []
            for i in range(lowest, highest + 1):
                left_trees = dfs(lowest, i - 1) 
                right_trees= dfs(i + 1, highest)
                for l in left_trees:
                    for r in right_trees:
                        temp = TreeNode(i)
                        temp.left = l
                        temp.right = r
                        tn_list.append(temp)

            return tn_list
     
        return dfs(1, n)