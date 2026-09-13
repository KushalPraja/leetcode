class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        overlaps = 0
        rows = len(img1)
        cols = len(img1[0])
        
        def check_overlap(img1, img2):
            nonlocal overlaps
            temp = 0
            for r in range(rows):
                for c in range(cols):
                    if img1[r][c] == img2[r][c] == 1:
                        temp += 1
            overlaps = max(overlaps, temp)

                        
        def shift_up(img, rows, cols):
            return img[1:] + [[0] * cols]
        
        def shift_down(img, rows, cols):
            return [[0] * cols] + img[:-1]
        
        def shift_left(img):
            return [row[1:] + [0] for row in img]
        
        def shift_right(img):
            return [[0] + row[:-1] for row in img]
        
        up = img1[:]
        down = img1[:]
        check_overlap(img1, img2)

        for i in range(rows):
            left = up
            right = up

            for j in range(cols):
                check_overlap(left, img2)
                left = shift_left(left)

            for j in range(cols):
                check_overlap(right, img2)
                right = shift_right(right)

            left = down
            right = down

            for j in range(cols):
                check_overlap(left, img2)
                left = shift_left(left)

            for j in range(cols):
                check_overlap(right, img2)
                right = shift_right(right)

            up = shift_up(up, rows, cols)
            down = shift_down(down, rows, cols)

        return overlap
