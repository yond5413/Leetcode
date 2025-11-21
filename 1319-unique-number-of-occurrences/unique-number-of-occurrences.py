from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        lookup = Counter(arr)
        vals_set = set(lookup.values())
        return len(vals_set) == len(lookup)