class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        ret = float("inf")
        w1 = None
        w2 = None
        for idx,i in enumerate(wordsDict):
            if i == word1:
                w1 = idx
            elif i == word2:
                w2 = idx
            #print(f"i:{i},idx:{idx},w1:{w1},w2:{w2}")
            if w1!=None and w2!=None:
                ret = min(abs(w2-w1),ret)
                print(ret)
        ret = min(abs(w2-w1),ret)
        return ret