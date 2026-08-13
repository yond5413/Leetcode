class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1,min2 = float("inf"),float("inf")
        for i in range(len(nums)):
            if min1>=nums[i]:
                min1 = nums[i]
            elif min2>=nums[i]:
                min2 = nums[i]
            else:
                return True
        return False