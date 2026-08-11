class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]*(n)
        for i in range(1,n):
            pre[i] = nums[i-1]*pre[i-1]
        print(pre)
        post = 1
        ret = [0]*n
        print(ret)
        for i in range(n-1,-1,-1):
            ret[i] = pre[i]*post
            post*=nums[i]
            
        return ret