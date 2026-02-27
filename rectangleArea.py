# finds the area of overlap between two rectangles

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)

        # checks if the two rectangles dont overlap
        if ax2 <= bx1 or by2 <= ay1 or bx2 <= ax1 or by1 >= ay2:
            return area1 + area2

        min_x = max(by1, ay1)
        max_x = min(ay2, by2)
        min_y = max(ax1, bx1)
        max_y = min(ax2, bx2)
        colliding_area = (max_x - min_x) * (max_y - min_y)
        return area1 + area2 - colliding_area