class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1 for _ in range(n)]
        for i in range(1,len(nums)):
            pre[i] = pre[i-1]*nums[i-1]
        post = 1
        ret = [0]*n
        for i in range(n-1,-1,-1):
            ret[i] = post*pre[i]
            post*=nums[i]
        return ret
