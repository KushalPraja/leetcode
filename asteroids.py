from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        x= []

        for i in asteroids:
            x.append(i)

            while len(x) >= 2 and (x[-1]<0 and x[-2]>0):
                temp = x[-1]
                x.pop()
                if abs(temp) == abs(x[-1]):
                    x.pop()
                else:
                    x[-1] = temp if max(abs(x[-1]), abs(temp)) == abs(temp) else x[-1]

        return x
