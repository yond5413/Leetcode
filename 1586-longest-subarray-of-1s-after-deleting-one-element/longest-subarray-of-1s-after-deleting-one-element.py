class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ret = 0
        flips = 1
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                flips-=1
            if flips<0:
                while flips<0:
                    if nums[l]==0:
                        flips+=1
                    l+=1
            ret = max(r-l,ret)
        return ret