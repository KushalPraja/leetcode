class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        mem = {}
        def dfs(r, c, moves):
            if not 0 <= r < m or not 0 <= c < n:
                return 1

            if (r, c, moves) in mem:
                return mem[(r,c, moves)]

            if moves == 0:
                return 0

            count = 0
            
            for x,y in [(0,1), (1,0), (-1,0), (0,-1)]:
                count += dfs(r + x, c + y, moves -1)

            mem[(r,c, moves)] = count

            return count

        return dfs(startRow,startColumn, maxMove) % (10**9 + 7) 
        

            