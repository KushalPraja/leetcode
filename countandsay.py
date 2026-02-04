class Solution:
    def countAndSay(self, n: int) -> str:
        curr = "1"
        for _ in range(n-1):
            curr = self.getrle(curr)
        
        return curr

    def getrle(self, s):
        res = ""
        count = 1
        curr = s[0]

        for i in range(1, len(s)):
            if s[i] == curr:
                count += 1
            
            else:
                res+= str(count)
                res+= str(curr)
                curr = s[i]
                count = 1
        
        res+= str(count)
        res+= str(curr)
    
        count = 1

        return res

