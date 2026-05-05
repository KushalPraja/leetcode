# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        

        n = 0
        curr = head

        while curr != None:
            n+=1
            curr = curr.next

        if k == 0 or n ==0 :
            return head
            
        k = k % n

        prev = None
        curr = head
        counter = n - k

        while counter != 0:
            prev = curr
            curr = curr.next
            counter -= 1

        prev.next = None

        if curr:
            temp = curr
            while temp and temp.next != None:
                temp = temp.next
            
            temp.next = head
            return curr

        return head
