class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dups = set()
        l,r = 0,0
        ret = 0
        while (r<len(s)):
            while s[r] in dups:
                dups.remove(s[l]) 
                l+=1
            dups.add(s[r])
            ret = max(ret,r-l+1)
            r+=1
        return ret