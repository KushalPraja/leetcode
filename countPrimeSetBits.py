import math

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
       
        count = 0

        def isprime(n):
            if n < 2:
                return False
            if n in (2, 3):
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False

            limit = int(math.sqrt(n)) + 1
            for i in range(5, limit, 6):
                if n % i == 0 or n % (i + 2) == 0:
                    return False
            return True

        for i in range(left, right + 1):
            bin_var = bin(i)
            temp = 0
            for i in bin_var[2:]:
                if i == "1":
                    temp += 1
            print(bin_var, temp)
            if isprime(temp):
                count += 1

        return count
