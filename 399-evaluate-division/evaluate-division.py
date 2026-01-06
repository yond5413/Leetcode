from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(dict)
        for i in range(len(equations)):
            u,v = equations[i]
            adj[u][v] = values[i]
            adj[v][u] = 1/values[i]
        ###################################
        def dfs(root,target,visited):
            if root not in adj and target not in visited:
                return -1
            if target in adj[root]:
                return adj[root][target]
            visited.add(root)
            for v in adj[root]:
                cost = adj[root][v]
                if v not in visited:
                    val = dfs(v,target,visited)
                    if val !=-1:
                        return val*cost
            return -1
        ret = []
        for u,v in queries:
            ret.append(dfs(u,v,set()))
        return ret

        