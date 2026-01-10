import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        q1,q2 = [],[]
        l,r = 0,len(costs)-1
        ret = 0
        for i in range(k):
            while len(q1)< candidates  and l<=r:
                heapq.heappush(q1,costs[l])
                l+=1
            while len(q2)< candidates  and l<=r:
                heapq.heappush(q2,costs[r])
                r-=1
            val1 = q1[0] if q1 else float("inf")
            val2 = q2[0] if q2 else float("inf")
            if val1<=val2:
                ret+=heapq.heappop(q1)
            else:
                ret+=heapq.heappop(q2)

        return ret