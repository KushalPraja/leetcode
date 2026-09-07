class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited = set()
    
        n = len(isConnected)

        def dfs(city):
            visited.add(city)

            for i in range(n):
                if isConnected[city][i] and i not in visited:
                    dfs(i)

        connections = 0
        for city in range(len(isConnected)):
            if city not in visited:
                dfs(city)
                connections +=1 

        return connections

