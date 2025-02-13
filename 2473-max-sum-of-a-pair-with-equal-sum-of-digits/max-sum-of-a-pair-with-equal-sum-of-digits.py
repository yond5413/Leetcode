import heapq
from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ret = -1
        lookup = defaultdict(list)
        for i in range(len(nums)):
            curr = nums[i]
            key = 0
            while(curr>0):
                key += curr%10
                curr //=10
            heapq.heappush(lookup[key],-nums[i])
        keys = list(lookup.keys())
        for k in keys:
            if len(lookup[k])>=2:
                curr = -1*heappop(lookup[k])
                curr -= heappop(lookup[k])
                ret = max(ret,curr)
        return ret
