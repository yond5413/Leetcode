class Solution:
    def reverseWords(self, s: str) -> str:
        curr = s.split()
        l,r  = 0,len(curr)-1
        while (l<=r):
            curr[l],curr[r] = curr[r],curr[l]
            r-=1
            l+=1
            print(curr)
        return " ".join(curr)