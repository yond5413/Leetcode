class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ret = 0
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] +=1
            else:
                freq[i] =1
        for i in range(len(nums)):
            curr = nums[i]
            targ = k-curr
            if freq.get(targ,0)>0 and freq.get(curr,0) >0:
                if targ == curr and freq[curr]<2:
                    continue
                freq[curr] -=1
                freq[targ]-=1
                ret+=1
        return ret