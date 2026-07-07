class Solution:
    def sumAndMultiply(self, n: int) -> int:
        
        ttl = 0
        digits = []
        while n:
            x = n % 10
            n //= 10

            if x != 0:
                ttl += x
                digits.append(str(x))

        if not digits:
            return 0
        return int("".join(digits[::-1])) * ttl
        
    

            