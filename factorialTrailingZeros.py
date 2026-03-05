'''
idea is that a number that has zeros can be divided by 10
10 has factors 5 and 2 

10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

2 factors of 5, 5 factors of 2
thus max amount of pairs of 2, 5 we can make is 2

powers also have their own factor that make additional 10s
25, 125
'''

class Solution:
    def trailingZeroes(self, n: int) -> int:

        count = 0
        temp = 5

        while n // temp > 0:
            count += n // temp
            temp *= 5

        return count
        
