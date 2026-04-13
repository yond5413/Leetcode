class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ret = float("inf")
        for i in range(len(nums)):
            if nums[i] == target:
                ret = min(ret,abs(i-start))

        return ret