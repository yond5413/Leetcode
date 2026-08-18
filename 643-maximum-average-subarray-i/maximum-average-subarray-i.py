class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[:k])
        ret = curr/k
        l,n = 0,len(nums)
        for r in range(k,n):
            curr += nums[r]
            curr -= nums[l]
            ret = max(ret,curr/k)
            l+=1
        return ret
