class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for idx,i in enumerate(nums):
            print(f"i:{i},idx:{idx}")
            curr = target-i
            if curr in lookup:
                if idx != lookup[curr]:
                    return [lookup[curr],idx]
            else:
                lookup[i]=idx