class Solution:
    def findMin(self, nums: List[int]) -> int:
        ret = nums[0]
        n = len(nums)
        l,r = 0,len(nums)-1
        while (l<=r):
            mid = (l+r)//2
            ret = min(ret,nums[mid])
            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid-1

        return ret