from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ret = []
        adj= defaultdict(dict)
        for i in range(len(equations)):
            u,v = equations[i]
            adj[u][v] = values[i]
            adj[v][u] = 1/values[i]
        def dfs(root,target,visited):
            if root not in adj or target not in adj:
                return -1
            if target in adj[root]:
                return adj[root][target]
            visited.add(root)
            ##########################
            for vert in adj[root]:
                cost = adj[root][vert]
                if vert not in visited:
                    val = dfs(vert,target,visited)
                    if val !=-1:
                        return val*cost
            return -1 
        for i in range(len(queries)):
            u,v = queries[i]
            ret.append(dfs(u,v,set()))
        ############################
        return ret