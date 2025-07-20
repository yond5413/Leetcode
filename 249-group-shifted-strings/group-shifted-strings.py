from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        for s in strings:
            if len(s) <=1:
                lookup[-1].append(s)
            else:
                diff_array = []
                for i in range(1,len(s)):
                    diff_array.append((ord(s[i])-ord(s[i-1]))%26)
                lookup[tuple(diff_array)].append(s)
        return list(lookup.values())