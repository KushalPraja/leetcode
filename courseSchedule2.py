from typing import List

# Kahn's algorithm implementation for topological sort

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = {}
        indegree = [0] * numCourses 
        for i, j in prerequisites:
            if j not in adj:
                adj[j] = []

            adj[j].append(i)
            indegree[i] += 1

        x = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                x.append(i)


        x = deque(x)
        res = []
        while x:
            curr = x.popleft()
            res.append(curr)

            if curr in adj:
                for i in adj[curr]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        x.append(i)

        if len(res) != numCourses:
            return []

        return res



                
           