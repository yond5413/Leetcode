class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for idx,i in enumerate(nums):
            curr = target-i
            if curr in lookup and lookup[curr] != idx:
                return [lookup[curr],idx]
            else:
                lookup[i] = idx