class Solution:
    def checkwindow(self, map1, map2):
        for i in map2.keys():
            if i not in map1:
                return False
            if i in map1:
                if map2[i] > map1[i]:
                    return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        r = 0
        l = 0
        mapping = {}
        for i in t:
            if i not in mapping:
                mapping[i] = 0
            mapping[i] += 1
        string = None
        map1 = {}
        while r < len(s):
            if s[r] not in map1:
                map1[s[r]] = 0
            map1[s[r]] += 1
            r+=1 

            while self.checkwindow(map1, mapping):
                map1[s[l]] -= 1
                l += 1
                if not string:
                    string = s[l-1:r]
                elif len(s[l-1:r]) < len(string):
                    string = s[l-1:r]

        return string if string else ""
