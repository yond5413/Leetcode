import heapq
# min_heap
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclid(point):
            ret = ((point[0])**2 + (point[1]**2))**(1/2)
            return ret
        heap = []
        for p in points:
            dist = euclid(p)
            heapq.heappush(heap,(-dist,p))
            if len(heap)>k:
                heapq.heappop(heap)
        ret = [i[1] for i in heap]
        return ret

        