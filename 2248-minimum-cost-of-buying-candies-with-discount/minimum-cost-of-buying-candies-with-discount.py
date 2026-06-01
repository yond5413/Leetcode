import heapq
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        new_cost = [cost[i]*-1 for i in range(len(cost))]
        heapq.heapify(new_cost)
        print(new_cost)
        ret = 0
        while new_cost:
            ret+= -heapq.heappop(new_cost)
            ret+= -heapq.heappop(new_cost) if new_cost else 0
            if new_cost:
                heapq.heappop(new_cost)
            
        return ret