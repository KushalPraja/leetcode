# Definition for singly-linked list.

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = None
        curr = head
        nxt = head.next

        crit_points = []
        dis = 0

        while nxt:
            prev = curr
            curr = nxt
            dis += 1
            nxt = nxt.next

            if prev and curr and nxt and ((prev.val < curr.val and nxt.val < curr.val) or (prev.val > curr.val and nxt.val > curr.val)):
                crit_points.append(dis)

        if not crit_points or len(crit_points) == 1:
            return [-1, -1]

        else: 
            min_dis = float('inf')
            max_dis = 0

            for i in crit_points:
                for j in crit_points:
                    if i != j:
                        min_dis = min(abs(i - j), min_dis)
                        max_dis = max(abs(i - j), max_dis)

        return [min_dis, max_dis]


 