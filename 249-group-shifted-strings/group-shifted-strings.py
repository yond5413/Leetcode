from collections import defaultdict
class Solution:
    ##FOr tracking the sequences/making key for hashmap 
    ## Either diff array like we have
    ## OR we can normalize around a
    ### Basically make first char of str a and offset others likewise
    #### offset will be between 0-25 
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        for s in strings:
            if len(s) == 1:
                lookup[-1].append(s)
            else:
                char_store = []
                i = 1
                while i<len(s):
                    char_store.append((ord(s[i])-ord(s[i-1]))%26)
                    i+=1
                seq = tuple(char_store)
                lookup[seq].append(s)
        return list(lookup.values())