class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r= 0,len(nums)
        while(l<=r):
            mid = (r+l)//2
            left = nums[mid-1] if mid-1>=0 else float("-inf")
            right = nums[mid+1] if mid+1<len(nums) else float("-inf")
            if left<=nums[mid] and right<=nums[mid]:
                return mid
            elif right>nums[mid]:
                l = mid+1
            else:
                r = mid-1
        return l