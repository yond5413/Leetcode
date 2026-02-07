class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        b_left = 0
        a_right = s.count("a")
        ret = min(n,b_left+a_right)
        for i in range(n):
            if s[i] == "a":
                a_right-=1
            else:
                b_left+=1
            ret = min(ret,b_left+a_right)
        return ret