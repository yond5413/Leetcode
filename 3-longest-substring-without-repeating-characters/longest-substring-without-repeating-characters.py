class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        ret = 0
        lookup = set()
        for r in range(len(s)):
            while s[r] in lookup:
                lookup.remove(s[l])
                l+=1
            lookup.add(s[r])
            ret = max(ret,r-l+1)
        return ret