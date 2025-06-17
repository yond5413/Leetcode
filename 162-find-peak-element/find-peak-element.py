class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1
        while(l<=r):
            mid = (l+r)//2
            left = float('-inf') if mid-1<0 else nums[mid-1]
            right = float('-inf') if mid+1>n-1 else nums[mid+1]
            if nums[mid]>right and nums[mid]>left:
                return mid
            elif nums[mid]>right:
                r = mid-1
            else:
                l = mid+1
        return mid-1
            