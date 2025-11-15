class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        curr = 0
        for i in range(k):  
            curr +=nums[i]
        l = 0
        ret = curr/k
        for r in range(k,n):
            curr += nums[r]
            curr -=nums[l]
            l+=1
            ret = max(curr/k,ret)
        return ret
