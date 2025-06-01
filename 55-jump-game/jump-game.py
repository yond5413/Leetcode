class Solution:
    def canJump(self, nums: List[int]) -> bool:
        count = 1
        for i in range(len(nums)):
            if count ==0:
                return False
            count = max(count-1,nums[i])
        return True