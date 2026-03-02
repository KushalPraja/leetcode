
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        string = ""

        for i in range(1, n + 1):
            binary = bin(i)[2:]
            string += binary

        return int(string, 2) % (10**9 + 7)
