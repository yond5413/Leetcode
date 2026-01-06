from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(dict)
        for i in range(len(equations)):
            u,v = equations[i]
            adj[u][v] = values[i]
            adj[v][u] = 1/values[i]
        ##################################
        def dfs(curr,target,visited):
            if curr not in adj or target not in adj:
                return -1
            if target in adj[curr]:
                return adj[curr][target]
            visited.add(curr)
            for v in adj[curr]:
                cost = adj[curr][v]
                if v not in visited:
                    val = dfs(v,target,visited)
                    if val !=-1:
                        return val*cost
            return -1
        ret = []
        for u,v in queries:
            ret.append(dfs(u,v,set()))
        return ret