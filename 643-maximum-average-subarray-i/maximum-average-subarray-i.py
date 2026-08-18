class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        curr = sum(nums[:k])
        print(curr)
        ret = curr/k
        l = 0
        for r in range(k,n):
            curr+=nums[r]
            curr-=nums[l]
            l+=1
            ret = max(curr/k,ret)
        return ret