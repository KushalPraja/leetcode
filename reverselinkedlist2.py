from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        curr = head
        prev = None
        for _ in range(left-1):
            prev = curr
            if curr:
                curr = curr.next
        
        temp_prev = prev
        prev = None

        pos = 0 
        while (curr):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            if pos == (right - left):
                break
            pos+=1
         
        if temp_prev:
            temp_prev.next = prev
        else:
            head = prev
        while prev and prev.next:
            prev = prev.next
        
        if prev and curr:
            prev.next = curr    

        
        return head
