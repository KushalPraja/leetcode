import math

class Solution:
    def countTriples(self, n: int) -> int:
        count = 0

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if math.sqrt(i ** 2 + j ** 2) % 1 == 0 and math.sqrt(i ** 2 + j ** 2) <= n:
                    count += 1

        return count