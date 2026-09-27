class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []
        temp_list = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)

            if s[i] == ")":
                curr = stack[-1]
                stack.pop()
                temp_list.append((curr, i))


        s = list(s)
        for i, j in temp_list:
            s[i + 1:j] = reversed(s[i + 1:j])
        
        curr = []
        for i in range(len(s)):
            if s[i] == ")" or s[i] == "(":
                continue
            curr.append(s[i])
        return "".join(curr)




