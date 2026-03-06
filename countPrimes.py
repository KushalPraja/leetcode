# sieve of eratosthenes algorithm (optimized)

class Solution:
    def countPrimes(self, n: int) -> int:

        if n <= 2:
            return 0

        temp = [True] * n
        temp[0], temp[1] = False, False

        for i in range(2, int(n**0.5)+1):
            if temp[i]:
                for j in range(i*i, n, i):
                    temp[j] = False
        
        return sum(temp)
