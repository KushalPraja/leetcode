class Solution:
    def reverseBits(self, n: int) -> int:
        x = format(n, 'b')
        y = ""
        for i in x[::-1]:
            y+= i
        while len(y) != 32:
            y += "0"
        return int(y, 2)
