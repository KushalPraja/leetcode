class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        temp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        max_area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == "1":
                    min_amount = "1"

                    if (i >= 1 and j >= 1):
                        directions = [(-1,0), (0, -1), (-1, -1)]
                        min_amount= str(1 +  min(int(temp[i - 1][j]), int(temp[i-1][j - 1]), int(temp[i][j-1])))

                    temp[i][j] = min_amount
                    max_area = max(int(min_amount) ** 2, max_area)
        
        return max_area