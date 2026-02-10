class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def dfs(start, path):
            if sum(path) >= target:
                if sum(path) == target:
                    res.append(path[:])

                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(i + 1, path)
                path.pop()
        
        dfs(0, [])
        return res