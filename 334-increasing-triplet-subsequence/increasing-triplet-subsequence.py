class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        min1 = float("inf")
        min2 = float("inf")
        for i in range(len(nums)):
            if min1 >= nums[i]:
                min1 = nums[i]
            elif min2>=nums[i]:
                min2 = nums[i]
            else:
                return True
        return False

