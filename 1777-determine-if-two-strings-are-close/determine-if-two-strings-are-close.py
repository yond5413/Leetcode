from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        lookup1 = Counter(word1)
        lookup2 = Counter(word2)
        vals1 = Counter([v for v in list(lookup1.values())])
        vals2 = Counter([v for v in list(lookup2.values())])
        return set(lookup1.keys())==set(lookup2.keys()) and vals1 == vals2