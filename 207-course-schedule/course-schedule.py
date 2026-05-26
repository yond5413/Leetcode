from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u,v in prerequisites:
            adj[v].append(u)
        visited = set()
        cache = {}
        def dfs(curr):
            if curr in visited:
                return False
            if curr in cache:
                return cache[curr]
            visited.add(curr)
            pre = adj[curr]
            for u in pre:
                if not dfs(u):
                    cache[u] = False
                    return False
            visited.remove(curr)
            cache[curr] = True
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True