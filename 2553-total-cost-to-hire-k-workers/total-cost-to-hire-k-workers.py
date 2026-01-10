class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        q1,q2 = [],[]
        ret = 0
        l,r = 0,len(costs)-1
        for _ in range(k):
            while len(q1)<candidates and l<=r:
                heapq.heappush(q1,costs[l])
                l+=1
            while len(q2)<candidates and l<=r:
                heapq.heappush(q2,costs[r])
                r-=1
            v1 = q1[0] if q1 else float("inf")
            v2 = q2[0] if q2 else float("inf")
            if v1<=v2:
                ret += heapq.heappop(q1)
            else:
                ret += heapq.heappop(q2)
        return ret