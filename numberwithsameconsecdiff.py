
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = set()
        def dfs(path):
            print(path)
            if len(path) == n:
                temp = int("".join([str(i) for i in path]))
                res.add(temp)
                return
            temp = path[-1]
            if (temp - k) >= 0:
                path.append(temp - k)
                dfs(path)
                path.pop()
            if (temp + k) < 10:
                path.append(temp + k)
                dfs(path)
                path.pop()
        for i in range(1, 10):
            dfs([i]) 
        return sorted(list(res))
