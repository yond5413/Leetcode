from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for crs,pre in prerequisites:
            adj[crs].append(pre)
        visited,cycle = set(),set()
        # not visited
        # visited
        #visiting
        def dfs(curr):
            if curr in visited:
                return True
            if curr in cycle:
                return False
            cycle.add(curr)
            for i in adj[curr]:
                if not dfs(i):
                    return False
            cycle.remove(curr)
            visited.add(curr)
            ret.append(curr)
            return True
        ret = []
        for i in range(numCourses):
            if not dfs(i):
                return []
        return ret