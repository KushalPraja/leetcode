# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        nodes = {}
        pos = 0
        curr = head
        while curr:
            if curr.next and curr.next in nodes:
                return nodes[curr.next]
            
            nodes[curr] = curr
            pos += 1
            curr = curr.next

        return None