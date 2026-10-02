class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        res = []

        def backtrack(opn, close, path):
            if opn + close == n * 2: 
                res.append(path)
                return

            if opn != n:
                backtrack(opn + 1, close, path + "(")

            if opn > close:
                backtrack(opn, close + 1, path + ")")

        backtrack(0, 0, "")
        return list(res)



