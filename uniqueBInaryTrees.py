class Solution:
    def numTrees(self, n: int) -> int:
        
        mem = {}

        def dfs(lowest, highest):
            if lowest > highest:
                return 1

            if (lowest, highest) in mem:
                return mem[(lowest, highest)]
         
            total = 0
            for i in range(lowest, highest + 1):
                l = dfs(lowest, i - 1) # possible combinations in left
                r = dfs(i + 1, highest) # combinations in right
                total += l * r
            
            mem[(lowest, highest)] = total
            return total
        
        return dfs(1, n)
