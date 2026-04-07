class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for l in range(len(haystack) - len(needle) + 1):
            if haystack[l:l + len(needle)] == needle:
                return l

        return -1
           