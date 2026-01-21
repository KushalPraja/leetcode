class Solution:
    def maxArea(self, heights: list[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        max_area = 0
        while(left < right):
            area = min(heights[left], heights[right]) * (right - left)
            max_area = max(area, max_area)
            
            if heights[left] == heights[right]:
                left += 1
                right -=1 

            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return max_area

x = Solution().maxArea([1,7,2,5,4,7,3,6])
print(x) #36
