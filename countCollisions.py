class Solution:
    def countCollisions(self, directions: str) -> int:
        if len(directions) < 2:
            return 0
        
        count = 0
        stack = []
    
        for i in range(len(directions)):
            curr = directions[i]
            if curr == "R":
                stack.append("R")
    
            elif curr == "S":
                while stack and stack[-1] == "R":
                    count += 1
                    stack.pop()
                stack.append("S")
    
            else:
                if not stack:
                    continue
                if stack[-1] == "S":
                    count += 1
                elif stack[-1] == "R":
                    count += 2
                    stack.pop()
                    while stack and stack[-1] == "R":
                        count += 1
                        stack.pop()
                
                stack.append("S")
    
        return count