class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        
        if rowIndex == 0:
            return [1]
        
        curr_row = [1,1]
        for _ in range(rowIndex-1):
            new_row = [0]*(len(curr_row) + 1)
            new_row[0], new_row[-1] = 1, 1
            for j in range(1, len(new_row)-1):
                new_row[j] = curr_row[j] + curr_row[j-1]
            curr_row = new_row
        return curr_row
