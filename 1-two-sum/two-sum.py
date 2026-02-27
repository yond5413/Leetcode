class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(len(nums)):
            if nums[i] not in lookup:
                lookup[nums[i]] = i
            if target-nums[i] in lookup:
                if i != lookup[target-nums[i]]:
                    return [lookup[target-nums[i]],i]