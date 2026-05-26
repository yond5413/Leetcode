from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        cache = {}
        adj = defaultdict(list)
        for u,v in prerequisites:
            adj[v].append(u)
        def dfs(curr):
            if curr in visited:
                return False
            if curr in cache:
                return cache[curr]
            visited.add(curr)
            paths = adj[curr]
            for p in paths:
                if not dfs(p):
                    return False
            visited.remove(curr)
            cache[curr] = True
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True