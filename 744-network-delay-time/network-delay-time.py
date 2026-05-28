from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # u->v with some w
        # n nodes
        # k = start 
        # djkstra algo
        adj = defaultdict(list)
        for u,v,w in times:
            adj[u].append((w,v))

        visited = set()
        min_heap = [(0,k)]
        t = 0
        while min_heap:
            w1,v1 = heapq.heappop(min_heap)
            if v1 in visited:
                continue
            t = max(t,w1)
            visited.add(v1)
            for w2,v2 in adj[v1]:
                if v2 not in visited:
                    heapq.heappush(min_heap,(w1+w2,v2))
                
        print(f"{len(visited)}, n:{n}")
        return t if n == len(visited) else -1


