from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None

        curr = head
        next_node = curr.next

        if not next_node:
            return curr

        post_node = next_node.next if next_node.next else None
        next_node.next = curr
        curr.next = self.swapPairs(post_node)

        return next_node

