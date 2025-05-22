import heapq 
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        ### Sort
        queries.sort(key = lambda x:(x[0]))
        heap = []
        ### Gredily pick queries with farthest endpoint first
        #-> priority queue/heap 
        diff = [0]*(len(nums)+1)
        ops = 0
        j = 0
        for i,num in enumerate(nums):
            ops += diff[i]
            while j< len(queries) and queries[j][0]==i:
                heapq.heappush(heap,-queries[j][1])
                # min heap in python lib
                j+=1
            while ops < num and heap and -heap[0]>=i:
                ops +=1
                diff[-heappop(heap)+1] -=1
            if ops<num:
                return-1 
        ########################
        return len(heap)