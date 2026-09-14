class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        x1, y1, x2 , y2 = rec1
        X1, Y1, X2, Y2 = rec2

        if X1 >= x2 or X2 <= x1:
            return False

        if Y1 >= y2 or Y2 <= y1:
            return False

        return True
