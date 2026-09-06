class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        indegree = [0] * numCourses
        mapping = {}

        for i, j in prerequisites:
            if i not in mapping:
                mapping[i] = []

            mapping[i].append(j)
            indegree[j] += 1

        queue = deque([])
        for  i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        prereq = [set() for _ in range(numCourses)]
        
        while queue:
            curr = queue.popleft()
                
            if curr in mapping:
                for j in mapping[curr]:
                    prereq[j].add(curr)
                    prereq[j].update(prereq[curr])
                    indegree[j] -= 1
                    if indegree[j] == 0:
                        queue.append(j)

        res = []
        for i, j in queries:
            if i in prereq[j]:
                res.append(True)
                continue
            
            res.append(False)

        return res


               