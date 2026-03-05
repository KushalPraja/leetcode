class Solution:
    def countPrimes(self, n: int) -> int:

        if n <= 2:
            return 0

        temp = [0] * n
        count = 1

        for i in range(2, n):
            temp[i] = i

        curr = 2
        while (curr != len(temp)):
            if temp[curr] == -1:
                curr += 1
                continue

            count += 1
            for i in range(curr, len(temp), curr):
                temp[i] = -1
            curr += 1
            
        return count - 1



