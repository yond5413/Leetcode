class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l,r = 0,0
        vowels = set(["a","e","i","o","u"])
        ret =0
        curr = 0
        while(r<len(s)):
            if s[r].lower() in vowels:
                curr+=1
            if r-l==k:
                curr = curr if s[l].lower() not in vowels else curr-1
                l+=1
            ret = max(ret,curr)
            r+=1

        return ret