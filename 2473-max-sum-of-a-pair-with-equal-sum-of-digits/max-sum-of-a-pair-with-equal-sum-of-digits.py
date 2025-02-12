import heapq
from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ret = -1
        lookup = defaultdict(list)
        for i in range(len(nums)):
            key = 0
            temp = nums[i]
            while(temp>0):
                key += temp%10
                temp = temp//10
            heapq.heappush(lookup[key],-1*nums[i])
        #print(lookup)
        keys = list(lookup.keys())
        for k in keys:
            if len(lookup[k])>=2:
                curr = 0
                curr-=heapq.heappop(lookup[k])
                curr-=heapq.heappop(lookup[k])
                ret = max(curr,ret)
        return ret