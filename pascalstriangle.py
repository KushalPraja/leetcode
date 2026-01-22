
class Solution:
    def generate(self, numRows: int):
        total = []

        # base case 1 empty
        if numRows < 1:
            return total 

        # base case 2 -- 1
        total.append([1])
        x = [1,1]
        if numRows == 1:
            return total
        
        # inductive case
        total.append([1,1])
        row = x
        for _ in range(2, numRows):
            row = self.generate_row_from_prev(row)
            total.append(row)

        return total

    def generate_row_from_prev(self, prev_row):
        x = [0] * (len(prev_row) + 1)
        x[0] = 1
        x[-1] = 1
        for i in range(1, len(prev_row)): # 2 -> 1
            x[i] = prev_row[i-1] + prev_row[i]
        return x

print(Solution().generate(2))
