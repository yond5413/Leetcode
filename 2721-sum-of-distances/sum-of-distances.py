from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [0]*n
        ## arr[i] == sum(i-j) over all j such that
        ## nums[j] == nums[i] ad j!=i
        lookup = defaultdict(list)
        for i in range(n):
            lookup[nums[i]].append(i)
        for group in lookup.values():
            total = sum(group)
            prefix_total=0
            sz = len(group)
            for i,idx in enumerate(group):
                ret[idx] = total-prefix_total*2+idx*(2*i-sz)
                prefix_total+=idx
        return ret