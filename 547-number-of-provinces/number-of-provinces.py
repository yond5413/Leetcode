class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        ret = 0
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