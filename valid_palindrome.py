class Solution:
    def isPalindrome(self, s: str) -> bool:
        fmtstr = []
        for i in s:
            if i.isalnum():
                fmtstr.append(i.lower())
        
        left = 0
        right = len(fmtstr) - 1
        while (left < right):
            if fmtstr[left] != fmtstr[right]:
                return False
            left += 1;
            right -= 1;

        return True


print(Solution().isPalindrome("Was it a car or a cat I saw?"))

