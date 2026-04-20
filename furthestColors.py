class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_dis = 0

        for i in range(len(colors)):
            for j in range(len(colors) - 1, i + 1, -1):
                if colors[i] != colors[j]:
                    max_dis = max(j - i, max_dis)
                    break
        
        return max_dis
                   