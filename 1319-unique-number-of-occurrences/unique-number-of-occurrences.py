from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        lookup = Counter(arr)

        counts = set(lookup.values())

        return len(counts) == len(lookup) 