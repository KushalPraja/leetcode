class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        
        res = []

        def backtrack(path):
            if sum(path) >= target:
                if sum(path) == target and sorted(path) not in res: 
                    res.append(sorted(path[:]))
                return

            for i in range(len(candidates)):
                path.append(candidates[i])
                backtrack(path)
                path.pop()

        backtrack([])
        return res
            
