class Solution:
    def longestPalindrome(self, s: str) -> int:
        mapping = {}

        for i in s:
            if i not in mapping:
                mapping[i] = 0
            mapping[i] += 1
        
        count = 0
        unique_one = False
        for i in mapping.values():      
            if i // 2:
                count += i//2 * 2

            if not unique_one and i%2 != 0:
                count += 1
                unique_one = True
        
        return count