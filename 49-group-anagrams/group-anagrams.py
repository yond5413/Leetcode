class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}
        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted in lookup:
                lookup[s_sorted].append(s)
            else:
                lookup[s_sorted] = [s]
        ret = []
        for k in lookup.keys():
            ret.append(lookup[k])
        return ret