# Definition for singly-linked list.

from typing import Optional
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = 0
        if not curr:
            return head

        while (curr.next != None):
            count += 1
            curr = curr.next
        
        if count <= 1:
            return head

        temp = head
    
        for i in range(math.ceil(count/2)):
            next_node = temp.next
            temp.next = next_node.next
            curr.next = next_node
            curr = curr.next
            temp = temp.next
        
        curr.next = None
        return head


