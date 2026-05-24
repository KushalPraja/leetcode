from typing import List
from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        

        visited = [0] * len(arr)
        visited[start] = 1

        n = len(arr)
        # 2 

        queue = deque([start])

        while queue:
            idx = queue.popleft()

            if arr[idx] == 0:
                return True

            if (idx + arr[idx]) < n and visited[idx + arr[idx]] != 1:
                visited[idx + arr[idx]] = 1
                queue.append(idx + arr[idx])

            if (idx - arr[idx]) >=0 and visited[idx - arr[idx]] != 1:
                visited[idx - arr[idx]] = 1
                queue.append(idx - arr[idx])

        return False

# from typing import List

# class Solution:
#     def canReach(self, arr: List[int], start: int) -> bool:

#         visited = {}

#         def dfs(index):

#             if arr[index] == 0:
#                 return True
            
#             if index in visited:
#                 return visited[index]

#             right = False
#             left = False

#             visited[index] = False

#             if (index + arr[index]) < len(arr):
#                 right = dfs(index + arr[index])

#             if (index - arr[index]) >= 0:
#                 left = dfs(index - arr[index])

#             return right or left
        
#         return dfs(start)