class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        l,r = 0,0
        curr_max = 0
        n = len(nums)
        nums.sort()
        while(r<n):
            if nums[r]<=nums[l]*k:
                r+=1
                curr_max = max(curr_max,r-l)
            else:
                l+=1
        return n-curr_max