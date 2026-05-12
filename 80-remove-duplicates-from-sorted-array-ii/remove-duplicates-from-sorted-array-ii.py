class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 2
        for r in range(2,len(nums)):
            if nums[k-2] != nums[r]:
                nums[k] = nums[r]
                k+=1

        return k