from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_digits = len(digits)
        res = []
        mapping = {"2": "abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":
        "pqrs", "8":"tuv", "9":"wxyz"}
        def dfs(string, curr_idx):

            if num_digits == curr_idx:
                res.append(string)
                return
            
            curr_string = mapping[digits[curr_idx]]

            for i in curr_string:
                dfs(string + i, curr_idx + 1)
        
        if len(digits) > 0:    
            dfs("", 0)
        return res

if __name__ == "__main__":
    print(Solution().letterCombinations("34"))
