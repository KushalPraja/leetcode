from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        visited = {}

        def dfs(index):

            if arr[index] == 0:
                return True
            
            if index in visited:
                return visited[index]

            right = False
            left = False

            visited[index] = False

            if (index + arr[index]) < len(arr):
                right = dfs(index + arr[index])

            if (index - arr[index]) >= 0:
                left = dfs(index - arr[index])

            return right or left
        
        return dfs(start)