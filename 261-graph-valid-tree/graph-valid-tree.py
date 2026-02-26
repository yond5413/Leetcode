from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True 
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        def dfs(curr,prev):
            if curr in visited:
                return False
            visited.add(curr)
            for i in adj[curr]:
                if i == prev:
                    continue
                if not dfs(i,curr):
                    return False
            return True
        return dfs(0,-1) and n == len(visited)