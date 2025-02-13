import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ret = 0
        heapq.heapify(nums)
        while(nums[0]<k):
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            new_entry = min(x,y)*2 + max(x,y)
            heapq.heappush(nums,new_entry)
            ret +=1
        return ret
