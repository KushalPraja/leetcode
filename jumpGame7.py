from collections import deque
from typing import List

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:


        queue = deque([0])
        furthest = 0
        while queue:
            curr = queue.popleft()
            start = max(curr + minJump, furthest + 1)
            end = curr + maxJump

            for i in range(start, min(end + 1, len(s))):
                if i == len(s) - 1 and s[i] == '0':
                    return True

                if s[i] == '0':
                    queue.append(i)

            furthest = max(furthest, end)
        return False