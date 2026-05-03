class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        s = list(s)
        goal = list(goal)

        for i in range(len(s)):
            start = s[0]
            s = s[1:]
            s.append(start)
            
            if s == goal:
                return True

        return False