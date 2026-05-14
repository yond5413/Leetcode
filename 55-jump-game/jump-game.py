class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr=1 
        for i in range(len(nums)):
            if curr ==0:
                return False
            curr = max(nums[i],curr-1)
        return True
