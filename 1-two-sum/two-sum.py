class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        ret = []
        for i in range(len(nums)):
            lookup[nums[i]] = i
        for i in range(len(nums)):
            if (target - nums[i]) in lookup:
                if lookup[target - nums[i]]!=i:
                    return [lookup[target - nums[i]],i]
