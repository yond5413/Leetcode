class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,r = 0,0
        ret = 0
        flips = 0
        while(r<len(nums)):
            #print(f"flips:{flips},l:{l},r:{r},nums:{nums[l:r+1]},ret:{ret}")
            if nums[r] == 0:
                flips +=1  
            if  flips>k:
                ret = max(ret,r-l)
                while l<=r and flips>k:
                    if nums[l] == 0:
                        flips-=1
                    l+=1
                
            r+=1
        ret = max(ret,r-l)
        return ret