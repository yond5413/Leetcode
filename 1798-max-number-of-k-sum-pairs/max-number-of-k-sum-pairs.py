class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        lookup = {}
        ret = 0
        for n in nums:
            if n in lookup:
                lookup[n]+=1
            else:
                lookup[n] =1
        print(lookup)
        for i in range(len(nums)):
            targ = k-nums[i]
            if lookup.get(targ,0)>0 and lookup[nums[i]]>0:
                if nums[i]==targ and lookup[targ]<2:
                    continue
                else:
                    ret+=1
                    lookup[targ]-=1
                    lookup[nums[i]]-=1
        return ret