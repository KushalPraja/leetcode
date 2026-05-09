class Solution:
    def numTrees(self, n: int) -> int:
        dp = {0:1, 1:1}

        def dfs(n):
            if n in dp:
                return dp[n]

            count = 0 
            for i in range(n):
                left = i
                right = n - 1 - i

                count += dfs(left) * dfs(right)
            
            if n not in dp:
                dp[n] = count

            return count

        return dfs(n)
            



       