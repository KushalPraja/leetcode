class Solution:
    def convert(self, s: str, numRows: int) -> str:
        levels = {}
        curr = 1
        s = list(s)[::-1]
        increasing = True
        
        while s:
            temp = s[-1]
            s.pop()
            if curr not in levels:
                levels[curr] = ""
            levels[curr] += temp

            if curr == numRows:
                increasing = False
            if curr == 1:
                increasing = True
            if increasing:
                curr += 1
            else:
                curr -= 1

        final_str = ""
        for i in list(levels.values()):
            final_str += i

        return final_str
