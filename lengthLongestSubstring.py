class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        sub_set = []
        x = 0
        while (x != len(s)):
            if s[x] not in sub_set:
                sub_set.append(s[x])
                max_len = max(len(sub_set), max_len)
                x += 1
            else:
                while (sub_set and s[x] in sub_set):
                    sub_set.pop(0)
                sub_set.append(s[x])
                x += 1
                max_len = max(len(sub_set), max_len)

        return max_len

s = "aab" # 3
print(Solution().lengthOfLongestSubstring(s))
