class Solution:
    def judgeCircle(self, moves: str) -> bool:
        mapping = {"L":(1,0), "R": (-1,0), "U": (0,1) , "D": (0,-1)}
        sumx, sumy = 0,0
        for i in moves:
            dx, dy = mapping[i]
            sumx+=dx 
            sumy+=dy

        return sumx == 0 and sumy == 0
