from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        
        rights = []
        for i in range(len(grid)):
            count = 0
            for j in range(len(grid[i]) - 1, -1, -1):
                if grid[i][j] == 1:
                    break
                count += 1
            rights.append(count)
        
        length = len(rights)

    
        swaps = 0
        for i in range(length):
            # required number of zeros
            required = length - i - 1
            pos = i

            while pos != length:
                if rights[pos] >= required:
                    break
                pos += 1
            
            if pos == length:
                return -1
            
            # bubble switch backwards till it reaches corrrect positions
            while (pos != i):
                rights[pos], rights[pos - 1] = rights[pos - 1], rights[pos]
                swaps += 1
                pos -= 1

        return swaps
            
