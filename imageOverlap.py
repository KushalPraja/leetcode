class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        overlaps = 0
        rows = len(img1)
        cols = len(img1[0])

        img1set = []
        img2set = set()

        for i in range(rows):
            for j in range(cols):
                if img1[i][j] == 1:
                    img1set.append((i, j))
                if img2[i][j] == 1:
                    img2set.add((i, j))

        N = rows
        max_count = 0
        for i in range(-N, N):
            for j in range(-N, N):
                count = 0
                for a, b in img1set:
                    na = a + i
                    nb = b + j

                    if (na, nb) in img2set:
                        count += 1

                max_count = max(count, max_count)

        return max_count
