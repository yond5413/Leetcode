class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for u,v in tickets:
            adj[u].append(v)
        for k in adj.keys():
            adj[k].sort(reverse=True)
        ret = []
        def dfs(curr):  
            while adj[curr]:
                dfs(adj[curr].pop())
            ret.append(curr)
        dfs("JFK")
        return ret[::-1]