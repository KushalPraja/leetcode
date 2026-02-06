class Solution:
    def intToRoman(self, num: int) -> str:
        
        mapping = [(1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'), (10, 'X'), (40, 'XL'), (50, 'L'), (90, 'XC'), (100, 'C'), (400, 'CD'), (500, 'D'), (900, 'CM'), (1000, 'M')]

        mapping= mapping[::-1]
        string = ""

        for val, char in mapping:
            while num // val > 0:
                string+= char
                num -= val
        
        return string

