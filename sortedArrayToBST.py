# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if len(nums) == 1:
            x = TreeNode()
            x.val = nums[0]
            return x

        left = 0
        right = len(nums) - 1

        mid = (left + right) // 2

        root = TreeNode()
        root.val = nums[mid]

        if (len(nums) - 1 != mid):
            root.right = self.sortedArrayToBST(nums[mid+1: right+1])
        if (mid > 0):
            root.left = self.sortedArrayToBST(nums[left : mid])
        
        return root
        
