class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = max(len(word1),len(word2))
        ret = ""
        
        for k in range(n):
            if k<len(word1):
                ret+=word1[k]
            if k<len(word2):
                ret+=word2[k]    
        return ret