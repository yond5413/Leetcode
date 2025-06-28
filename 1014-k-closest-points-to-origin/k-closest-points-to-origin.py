import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclid(point):
            return ((point[0]**2)+(point[1]**2))**(1/2)
        heap = []
        for i in points:
            dist = euclid(i)
            heapq.heappush(heap,(-dist,i))
            if len(heap)>k:
                heapq.heappop(heap)
        ret = [i[1] for i in heap]
        return ret