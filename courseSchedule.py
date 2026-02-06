from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {}

        for need, prereq in prerequisites:
            if need == prereq:
                return False

            if not self.dfs(need, prereqs, prereq):
                return False

            if not prereq in prereqs:
                prereqs[prereq] = []

            prereqs[prereq].append(need)                
        
        return True
    
    def dfs(self, need, prereqs, prereq):
        if need not in prereqs:
            return True

        temp = prereqs[need]
        del prereqs[need]
        if prereq in temp:
            return False

        prereqs[prereq] = temp

        for i in temp:
            if not self.dfs(i, prereqs, prereq):
                return False

        return True
