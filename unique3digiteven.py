class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        temp = set()
        x = {}
        for i in digits:
            if str(i) not in x:
                x[str(i)] = 0
            x[str(i)] += 1

        def dfs(path):
            if len(path) >= 3:
                result = int("".join(str(num) for num in path))
                if result >= 100 and result % 2 == 0:
                    temp.add(result)
                return

            for i in range(len(digits)):
                if x[str(digits[i])] > 0:
                    x[str(digits[i])] -= 1
                    path.append(digits[i])
                    dfs(path)
                    path.pop()
                    x[str(digits[i])] += 1

        dfs([])
        return len(temp
