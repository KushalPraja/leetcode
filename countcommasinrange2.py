class Solution:
    def countCommas(self, n: int) -> int:

        commas = (len(str(n)) - 1) // 3

        if commas < 1:
            return 0

        x = [0] * (commas + 1)
        temp = 1000
        x[1] = 0

        for i in range(2, commas + 1):
            new_temp = temp * 1000
            x[i] = (new_temp - temp) * (i - 1) + 1
            temp = new_temp

        ttl = sum(x) + ((n - 1000 ** commas) * commas + 1)
        return ttl
