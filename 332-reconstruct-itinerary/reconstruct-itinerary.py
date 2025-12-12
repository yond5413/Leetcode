from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ret = []
        ## starts at jfk
        adj = defaultdict(list)
        for u,v in tickets:
            adj[u].append(v)
        for k in adj.keys():
            adj[k].sort()
        ret = []
        def dfs(curr):
            while adj[curr]:
                next_dest = adj[curr].pop(0)
                dfs(next_dest)
            ret.append(curr)

        dfs("JFK")
        return ret[::-1]    

            

