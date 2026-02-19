class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        arry = [1]
        curr = s[0]
        const = 0
        for i in s[1:]:
            if i == curr:
                arry[-1] += 1
            else:
                arry.append(1)
                curr = i
        
        for i in range(1,len(arry)):
            const += min(arry[i-1], arry[i])

        return const
        
