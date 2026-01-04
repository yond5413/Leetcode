class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ret=0
        n = len(isConnected)
        visited = set()
        def dfs(curr):
            visited.add(curr)
            for i in range(n):
                if isConnected[curr][i] and i not in visited:
                    dfs(i)
        for i in range(n):
            if i not in visited:
                ret+=1
                dfs(i)
        return ret