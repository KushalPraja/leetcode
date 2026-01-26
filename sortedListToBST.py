# Definition for singly-linked list.

from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
        def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:


            curr = head

            if not curr:
                return

            # base case
            if curr.next == None:
                x = TreeNode(curr.val)
                return x

            length = 0
            while (curr != None):
                length += 1
                curr = curr.next
    
            mid = length//2

            curr = head
            prev = None
            temp = 0

            while (temp != mid):
                temp+=1
                prev = curr
                curr = curr.next

            node = TreeNode(curr.val)
            if curr.next:
                node.right = self.sortedListToBST(curr.next)
            if head:
                prev.next = None
                node.left = self.sortedListToBST(head)
            return node

