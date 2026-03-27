class Solution:
    def shiftright(self, amountofshifts: int, row: list[int]):
        for i in range(len(row)):
            if row[abs((i+amountofshifts) % len(row))] != row[i]:
                return False
        return True


    def shiftleft(self, amountofshifts: int, row: list[int]):
        for i in range(len(row)):
            if row[abs((i-amountofshifts) % len(row))] != row[i]:
                return False
        return True

    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        for j in range(len(mat)):
            i = mat[j]
            if j % 2 == 0:
                if not self.shiftleft(k, i):
                    return False
            else:
                if not self.shiftright(k, i):
                    return False
        return True
   