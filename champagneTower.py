class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        curr = []
        curr.append([poured])
        i = 1
       
        
        for i in range(1, query_row + 1):
            new_row = [0] * (len(curr[-1]) + 1)
            for j in range(len(curr[-1])):
                remaining = curr[-1][j] - 1 

                if remaining>0:
                    new_row[j] += remaining / 2
                    new_row[j+1] += remaining/ 2

            curr.append(new_row[:])

        if curr[query_row][query_glass] > 1 :
            return 1

        return curr[query_row][query_glass] if curr[query_row][query_glass] > 0 else 0.0




