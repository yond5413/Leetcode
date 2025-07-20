from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cache = {}
        adj_list = defaultdict(list)
        for c,p in prerequisites:
            adj_list[p].append(c)
        def dfs(vert,visited):
            if vert in visited:
                return False
            if vert in cache:
                return cache[vert]
            visited.add(vert)
            for c in adj_list[vert]:
                if not dfs(c,visited):
                    cache[c] = False
                    return False
            visited.remove(vert)
            cache[vert] = True
            return True
        for i in range(numCourses):
            if not dfs(i,set()):
                return False
        return True