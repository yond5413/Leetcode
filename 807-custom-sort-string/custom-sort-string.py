from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        ret = ''
        for i in order:
            if i in freq:
                ret+= i*freq[i]
                freq.pop(i)
        for k in list(freq.keys()):
            ret+=freq[k]*k
        return ret