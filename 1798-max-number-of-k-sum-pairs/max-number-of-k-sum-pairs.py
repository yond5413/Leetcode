class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l,r = 0 ,len(nums)-1
        ret = 0
        nums.sort()
        while(l<r):
            if nums[l]+nums[r] ==k:
                ret+=1
                r-=1
                l+=1
            elif nums[l]+nums[r] >k:
                r-=1
            else:
                l+=1
        return ret