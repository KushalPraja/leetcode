from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
            
        res = []

        def dfs(string, closing_brackets, opening_brackets):
            if len(string) == n * 2:
                res.append(string)
                return

            if opening_brackets < n:
                dfs(string + "(", closing_brackets, opening_brackets + 1)

            if closing_brackets < opening_brackets:
                dfs(string + ")", closing_brackets + 1, opening_brackets)
    
        dfs("", 0, 0);
        return res;

if __name__ == "__main__":
    x = Solution().generateParenthesis(3)
    print(x)
                
        
