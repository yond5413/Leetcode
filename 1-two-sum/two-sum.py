class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(len(nums)):
            if target-nums[i] in lookup:
                if lookup[target-nums[i]] != i:
                    return[lookup[target-nums[i]],i]
            else:
                lookup[nums[i]] = i