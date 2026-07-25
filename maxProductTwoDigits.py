import math

class Solution:
    def maxProduct(self, n: int) -> int:

        digits = []

        while n:
            digits.append(n % 10)
            n = math.floor(n / 10)

        digits.sort(reverse=True)
        return digits[0] * digits[1]
