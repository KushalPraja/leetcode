from collections import deque, List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        

        mapping = {}
        for i in range(len(roads)):

            curr = roads[i][0]

            if curr not in mapping:
                mapping[curr] = []

            mapping[curr].append((roads[i][1],roads[i][2]))

            curr = roads[i][1]

            if curr not in mapping:
                mapping[curr] = []

            mapping[curr].append((roads[i][0],roads[i][2]))

        
        min_score = float('inf')

        visited = {1}
        queue = deque([1])

        while queue:
            curr = queue.popleft()

            for nxt, score in mapping[curr]:
                min_score = min(min_score, score)

                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)

        return min_score

        
 
