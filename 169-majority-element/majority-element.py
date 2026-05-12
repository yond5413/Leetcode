from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        freq = Counter(nums)
        for k in freq.keys():
            if freq[k] >= n/2:
                return k