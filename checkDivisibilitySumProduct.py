class Solution:
    def checkDivisibility(self, n: int) -> bool:
        
        sm = 0
        prd = 1

        for i in str(n):
            sm += int(i)
            prd *= int(i)

        return (n % (sm + prd) == 0)
