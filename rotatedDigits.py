class Solution:
    def rotatedDigits(self, n: int) -> int:
        dp = {
            "0": False,
            "1": False,
            "2": True,
            "5": True,
            "6": True,
            "8": False,
            "9": True}

        count = 0

        for i in range(1,n + 1):

            if i < 10:
                if str(i) in dp and dp[str(i)]:
                    count += 1
            
            else:
                first = i // 10
                last = i % 10
    
                if str(first) not in dp:
                    continue
                
                elif str(last) not in dp:
                    continue
    
                if dp[str(first)] or dp[str(last)]:
                    dp[str(i)] = True
                    count += 1
                else:
                    dp[str(i)] = False

        return count
