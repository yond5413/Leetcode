class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t): return False

        p1,p2 = 0,0
        while(p2<len(t) and p1 <len(s)):
            if t[p2] == s[p1]:
                p1+=1
                if p1 == len(s):
                    return True
            p2+=1
        return p1 == len(s)