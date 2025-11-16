class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        lookup = {"a":0,"e":0,"i":0,"o":0,"u":0}
        l = 0
        ret = 0
        count = 0
        for r in range(len(s)):
            if s[r].lower() in lookup:
                lookup[s[r].lower()]+=1
                count+=1
            if r-l+1 == k:
                ret = max(ret,count)
                if s[l].lower() in lookup:
                    count-=1
                    lookup[s[l].lower()]-=1
                l+=1
        return ret
