class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ret = 0
        l,r = 0,0
        n =len(nums)
        flips = 0
        while (r<n):
            if nums[r] ==0:
                flips = flips+1 
            while flips>k:
                    if nums[l] == 0:
                        flips-=1
                    l+=1
            ret = max(r-l+1,ret)
            r+=1
        return ret