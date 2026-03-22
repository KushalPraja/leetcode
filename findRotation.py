from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        array = [[] for _ in range(4)]

        for i in range(0, len(mat)):
            array[0].append([])
            array[1].append([])
            array[2].append([])
            array[3].append([])
            for j in range(0, len(mat)):
                array[0][-1].append(mat[i][j])
                array[1][-1].append(mat[len(mat)-i - 1][len(mat)-j - 1])
                array[2][-1].append(mat[j][len(mat)-i - 1])
                array[3][-1].append(mat[len(mat)-j-1][i])

        return target in array
                
