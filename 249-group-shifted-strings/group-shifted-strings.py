from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        for s in strings:
            if len(s) ==1:
                lookup[-1].append(s)
            else:
                ## the fun part
                char_store = []
                i = 1
                while i <len(s):
                    char_store.append((ord(s[i])-ord(s[i-1]))%26)
                    i+=1
                seq = tuple(char_store)
                lookup[seq].append(s)
        return list(lookup.values())