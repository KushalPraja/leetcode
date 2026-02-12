
class Solution:
    def longestBalanced(self, s: str) -> int:

        max_len = 0;

        for l in range(len(s)):

            freq = {}

            for r in range(l, len(s)):
                if s[r] not in freq:
                    freq[s[r]] = 1;
                else:
                    freq[s[r]] += 1;
                
                x = list(freq.values())
                good = True
                for i in range(len(x)):
                    if i > 0 and x[i] != x[i-1]:
                        good = False

                if good:
                    max_len = max(max_len, r - l + 1)

        return max_len



if __name__ == "__main__":
    print(Solution().longestBalanced("abbac"))
    print(Solution().longestBalanced("zzabccy"))
    print(Solution().longestBalanced("aba"))
                        









        
