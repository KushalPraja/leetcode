class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        waviness = 0

        for i in range(num1, num2 + 1):
            if len(str(i)) < 3:
                continue

            for j in range(1, len(str(i)) - 1):
                min_me = min(str(i)[j-1], str(i)[j+1]) 
                max_me = max(str(i)[j-1], str(i)[j+1])
    
                if  (max_me < str(i)[j]) or (min_me > str(i)[j]):
                    waviness += 1
                
        
        return waviness