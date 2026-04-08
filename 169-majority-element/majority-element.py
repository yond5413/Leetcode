from collections import Counter
import heapq
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        return heapq.nlargest(1,freq,key=freq.get)[-1]