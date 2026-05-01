# Definition for singly-linked list.
import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time complexity is O(N log k) where N is the total number of nodes in all lists and k is the number of lists.
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        head = ListNode(0)
        curr = head
        min_heap = []

        for i in range(len(lists)):
            if lists[i]:
                min_heap.append((lists[i].val, i))

        while min_heap:
            heapq.heapify(min_heap)
            val, index = min_heap[0]
            heapq.heappop(min_heap)
            curr.next = ListNode(val)
            if lists[index].next:
                lists[index] = lists[index].next
                heapq.heappush(min_heap, (lists[index].val, index))
            curr = curr.next
            
        return head.next