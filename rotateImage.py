from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in matrix:
            i.reverse()
        n = len(matrix)
        for i in range(n):
            for j in range(n-i):
                matrix[i][j], matrix[n -1 - j][n -1 -  i] = matrix[n -1 -  j][n - 1 - i], matrix[i][j]


        return matrix