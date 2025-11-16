class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ret = 0
        flips = 0
        l,r = 0,0
        while r<len(nums):
            if nums[r] !=1:
                flips +=1
            while flips >k :
                    if nums[l] !=1:
                        flips-=1
                    l+=1
            ret = max(r-l+1,ret)
            r+=1
        return ret