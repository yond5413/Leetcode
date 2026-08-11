class Solution:
    def reverseWords(self, s: str) -> str:
        new_s = s.split()
        l,r = 0, len(new_s)-1
        while (l<r):
            new_s[l],new_s[r] = new_s[r],new_s[l]
            l+=1
            r-=1
        return (" ").join(new_s)