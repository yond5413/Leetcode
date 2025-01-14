class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        '''
        setup adj_list
        dfs 
        tada
        '''
        adj_list = [[] for _ in range(n)]
        for i in range(n-1):
            u,v = connections[i][0], connections[i][1]
            adj_list[u].append((v,1))
            adj_list[v].append((u,-1))
        #visited = set()
        def dfs(adj,visited,curr_vert):
            total = 0
            if curr_vert not in visited:
                visited.add(curr_vert)
            for pair in adj[curr_vert]:
                vert,direction = pair
                if vert not in visited:
                    if direction !=-1:
                        total+=1
                    total += dfs(adj,visited,vert)
            return total
        return dfs(adj_list,set(),0)