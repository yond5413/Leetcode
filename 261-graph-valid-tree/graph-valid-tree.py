from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        def dfs(curr,prev):
            if curr in visited:
                return False
            visited.add(curr)
            for u in adj[curr]:
                if u == prev:
                    continue
                if not dfs(u,curr):
                    return False
            return True
        return dfs(0,-1) and len(visited) == n