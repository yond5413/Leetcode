class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ret = 0
        l = 0
        r = 0
        flips =1
        while(r<len(nums)):
            if nums[r] ==0:
                flips-=1    
            if flips<0:
                while flips<0:
                    if nums[l] == 0:
                        flips+=1
                    l+=1
            ret = max(ret,r-l)
            r+=1
        return ret