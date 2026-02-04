from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ls = [[0]* len(m) for m in triangle]
        
        ls[0][0] = triangle[0][0]

        for i in range(1, len(ls)):
            for j in range(len(triangle[i])):
                left = ls[i - 1][j-1] if 0 <= j - 1 < len(triangle[i - 1]) else float('inf')
                right = ls[i-1][j] if 0 <= j < len(triangle[i - 1]) else float('inf')
                ls[i][j] = min(left, right) + triangle[i][j]

        return min(ls[len(triangle)-1])