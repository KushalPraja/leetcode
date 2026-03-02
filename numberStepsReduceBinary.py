class Solution:
    def numSteps(self, s: str) -> int:
        
        x = int(s, 2)
        steps = 0

        while x != 1:
            if x % 2 == 0:
                x = x//2
            else:
                x += 1

            steps += 1
        
        return steps

