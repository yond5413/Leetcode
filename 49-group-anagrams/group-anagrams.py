class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        for s in strs:
            s_sorted = "".join(sorted(s))
            lookup[(s_sorted)].append(s)
        return [lookup[k] for k in lookup.keys()]