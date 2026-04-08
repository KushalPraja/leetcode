class Solution:
    def isHappy(self, n: int) -> bool:
        
        sm = n
        temp = 0
        mapping = set()

        while True:
            for idx in str(sm):
                temp += int(idx) ** 2
            
            if temp == 1:
                return True

            if temp in mapping:
                return False
            
            sm = temp
            mapping.add(temp)
            temp = 0
        
        return False
       