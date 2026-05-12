class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ret = 0
        n = len(nums)
        l = 0
        for r in range(n):
            if nums[r] != val:
                nums[l] = nums[r]
                ret+=1
                l+=1
        return ret