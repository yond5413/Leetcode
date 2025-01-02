class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        curr = 0
        for r in range(k):
            curr +=nums[r]
        ret = curr/k
        n = len(nums)
        for r in range(k,n):
            curr +=nums[r]
            curr-=nums[l]
            l+=1
            ret = max(ret,curr/k)
        return ret