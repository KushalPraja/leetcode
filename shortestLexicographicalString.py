class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        
        result = ""
        temp = []
        for i, val in enumerate(s):
            if val == "1":
                temp.append(i)

        min_val = float('inf')
        for i in range(len(temp) - k + 1):
            l = temp[i]
            r = temp[i + k - 1]
            min_val = min(min_val, r - l + 1)
            if min_val == r - l + 1:
                if not result:
                    result = s[l:r + 1]

                if len(result) >= len(s[l:r+1]) and int(result) > int(s[l:r+1]): 
                    result = s[l:r+1]
                
                

        return result

