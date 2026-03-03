from typing import List, Optional

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda item:item[0])
        stack = []

        for i in range(len(intervals)):

            if stack and intervals[i][0] <= stack[-1][1]:
                stack[-1][0] = min(stack[-1][0], intervals[i][0])
                stack[-1][1] = max(stack[-1][-1], intervals[i][-1])

            else:
                stack.append(intervals[i])

        return stack
        