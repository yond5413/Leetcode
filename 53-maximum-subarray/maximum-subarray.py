class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = nums[0]
        curr = ret
        n = len(nums)
        for i in range(1,n):
            curr = max(curr+nums[i],nums[i])
            ret = max(ret,curr)
        return ret