class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        def backtrack(curr_digit, digit, path):
            if len(path) == digit:
                return 1

            count = 0 
            if curr_digit == digit:
                for i in range(1, 10):
                    if str(i) not in list(path):
                        count += backtrack(curr_digit -1, digit, path + str(i))

            else:
                for i in range(0, 10):
                    if str(i) not in list(path):
                        count += backtrack(curr_digit -1, digit, path + str(i))

            return count

        temp = 0
        for i in range(0, n + 1):
            temp += backtrack(i, i, "")
        return temp