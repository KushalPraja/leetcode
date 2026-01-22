class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")":"(", "]":"[", "}":"{"}
        stack = []
        for i in s:
            if i in mapping:
                if stack and mapping[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        if stack == []:
            return True
        
        return False

print(Solution().isValid("()[]{}"))
