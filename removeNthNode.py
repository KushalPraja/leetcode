from typing import Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
    
        # get the size
        size = 0
        while curr != None:
            curr = curr.next
            size += 1

        curr = head
        prev = None

        for _ in range(size - n):
            prev = curr
            curr = curr.next

        if prev and curr:
            prev.next = curr.next
        elif prev:
            prev.next = None
        elif curr:
            return curr.next
        else:
            return None

        return head
