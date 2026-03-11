class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bin_n = bin(n)[2:]
        new_one = ""
        
        for i in range(len(bin_n)):
            if bin_n[i] == "1":
                new_one += "0"
            else:
                new_one += "1"
                
        return int(new_one, 2)