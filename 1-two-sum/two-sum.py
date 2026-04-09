class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(len(nums)):
            val = target-nums[i]
            if val in lookup and lookup[val] !=i:
                return [lookup[val],i]
            else:
                lookup[nums[i]] = i