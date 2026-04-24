class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l = 0
        r = 0 
        rand = 0
        for i in range(len(moves)):
            if moves[i] == "L":
                l += 1
            elif moves[i] == "R":
                r += 1
            else:
                rand += 1
        
        if l > r:
            return l + rand - r
        else:
            return r + rand - l
            