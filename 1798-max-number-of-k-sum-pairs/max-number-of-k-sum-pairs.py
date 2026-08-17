class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] = 1+freq.get(i,0)
            else: 
                freq[i] = 1
        print(freq)
        ret = 0
        for i in range(len(nums)):
            curr = nums[i]
            targ = k-curr
            if targ in freq and freq[targ]>0 and freq[curr]>0:
                if targ == curr and freq[targ]<2:
                    continue
                else:
                    ret+=1
                    freq[curr] -=1 
                    freq[targ] -= 1
        return ret