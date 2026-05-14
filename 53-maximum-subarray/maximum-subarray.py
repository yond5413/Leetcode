class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = float('-inf')
        curr = 0
        for i in range(len(nums)):
            curr = max(curr+nums[i],nums[i])
            ret = max(ret,curr)
        return ret