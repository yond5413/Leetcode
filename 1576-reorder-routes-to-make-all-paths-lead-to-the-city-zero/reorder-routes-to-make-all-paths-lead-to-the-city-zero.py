from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u,v in connections:
            adj_list[u].append((v,1))
            adj_list[v].append((u,-1))
        
        def dfs(adj,visited,curr):
            ret = 0
            visited.add(curr)
            for vert,direction in adj[curr]:
                if vert not in visited:
                    if direction ==1:
                        ret+=1
                    ret+= dfs(adj,visited,vert)
            return ret
        return dfs(adj_list,set(),0)