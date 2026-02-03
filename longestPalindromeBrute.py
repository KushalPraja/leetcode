class Solution:
    def longestPalindrome(self, s: str) -> str:

        def isPalindrome(s):
            return s == s[::-1]

        if len(s) == 1:
            return s
        max_palindrome = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome("".join(s[i:j+1])):
                    if len(s[i:j+1]) > len(max_palindrome):
                        max_palindrome = "".join(s[i:j+1])

        return max_palindrome
