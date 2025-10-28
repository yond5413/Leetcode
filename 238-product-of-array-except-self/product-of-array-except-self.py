class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]*n
        for i in range(1,n):
            pre[i] = pre[i-1]*nums[i-1]
        post = 1
        answer = [0]*n
        
        for i in range(n-1,-1,-1):
            answer[i] = pre[i]*post
            post*=nums[i] 
        return answer