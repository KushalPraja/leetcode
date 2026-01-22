# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        x = []

        while (head and head.next != None):

            if (head in x):
                return True

            x.append(head)
            head = head.next;
        
        return False
