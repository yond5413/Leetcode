class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        for i in nums:
            total+=i
        pre = 0
        for i in range(len(nums)):
            if pre == total-(nums[i]+pre):
                return i
            pre+=nums[i]
        return -1
