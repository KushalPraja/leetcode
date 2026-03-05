class Solution:
    def minOperations(self, s: str) -> int:

        count1 = 0
        count2 = 0
        start1 = "1"
        for i in s:
            curr = i
            if i != start1:
                count1 += 1
            if i == start1:
                count2 += 1

            if start1 == "1":
                start1 = "0"
            else:
                start1 = "1"
    
        return min(count1, count2)

