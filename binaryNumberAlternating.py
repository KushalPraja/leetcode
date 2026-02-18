class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binN = bin(n)

        curr = binN[2] if len(binN) >= 2 else None
        
        for i in binN[2:]:
            if i != curr:
                return False
            
            if curr == "1":
                curr = "0" 
            else:
                curr = "1"

        return True
                
