class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        ret = float("inf")
        w1 = None
        w2 = None
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                w1 = i
            if wordsDict[i] == word2:
                w2 = i
            if w1!=None and w2!=None:
                ret = min(ret,abs(w2-w1))
        return ret