from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        slow_curr = head

        while curr and curr.next:
            curr = curr.next.next
            slow_curr = slow_curr.next

        return slow_curr

