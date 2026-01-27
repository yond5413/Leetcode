from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        for i in range(len(strs)):
            s_sorted = "".join(sorted(strs[i]))
            lookup[s_sorted].append(strs[i])
        return [lookup[k] for k in lookup.keys()]