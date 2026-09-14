class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = set()

        def dfs(path, x):
            if x == n:
                res.add(tuple(path))
                return

            for i in range(1, len(path) + 1):
                temp = path
                path = path[:i] + "()" + path[i:]
                dfs(path, x + 1)
                path = temp


        if n == 0:
            return []
        
        dfs("()", 1)
        result = ["".join(i) for i in res]
        return result
