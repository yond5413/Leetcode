class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = 0
        lookup = set()
        l = 0
        for r in range(len(s)):
            while s[r] in lookup:
                lookup.remove(s[l])
                l+=1
            lookup.add(s[r])
            ret = max(r-l+1,ret)
        return ret
