from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
       ### top sort 
        adj_list = defaultdict(list)
        cache = {}
        for course,prereq in prerequisites:
            adj_list[prereq].append( course)
        ############################## 
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
            cache[vert] = True
            visited.remove(vert)
            return True
        for i in range(numCourses):
            if not dfs(i,set()):
                return False
        return True