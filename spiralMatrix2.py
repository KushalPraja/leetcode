from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        listy = [[0] * n for _ in range(n)]

        counter = 1

        x, y = 0, 0
        for i in range(n - 1, -1, -2):

            if i == 0:
                listy[x][y] = counter

            for _ in range(i):
                listy[x][y] = counter
                counter += 1
                y += 1

            for _ in range(i):
                listy[x][y] = counter
                counter += 1
                x += 1

            for _ in range(i):
                listy[x][y] = counter
                counter += 1
                y -=1

            for _ in range(i):
                listy[x][y] = counter
                counter += 1
                x -=1
            x += 1
            y += 1

        return listy