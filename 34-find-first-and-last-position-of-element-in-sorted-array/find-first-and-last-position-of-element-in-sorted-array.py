class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.bin_search(nums,target,True)
        r = self.bin_search(nums,target,False)
        return [l,r]

    def bin_search(self,nums,target,left_most):
        ret = -1
        l,r = 0,len(nums)-1
        while(l<=r):
            mid = (r+l)//2
            if nums[mid]==target:
                ret = mid
                if left_most:
                    r = mid-1 
                else:
                    l = mid+1

            elif nums[mid]>target:
                r = mid-1
            else:
                l = mid+1
        return ret