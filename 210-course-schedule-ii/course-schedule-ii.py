from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ret = []
        visited,cycle = set(),set()
        adj = defaultdict(list)
        for u,v in prerequisites:
            adj[v].append(u)
        def dfs(curr):
            if curr in cycle:
                return False
            if curr in visited:
                return True
            cycle.add(curr)
            for u in adj[curr]:
                if not dfs(u):
                    return False
            cycle.remove(curr)
            visited.add(curr)
            ret.append(curr)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        ret = ret[::-1]
        return ret