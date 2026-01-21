class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)



if __name__ == "__main___":

    s = "racecar"
    t = "carrace"

    print(Solution().isAnagram(s, t))
