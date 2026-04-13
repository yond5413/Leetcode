class Solution:
    def isPalindrome(self, x: int) -> bool:
        s_x = str(x)
        l,r = 0,len(s_x)-1
        while (l<=r):
            if s_x[l] != s_x[r]:
                return False
            l+=1
            r-=1
        return True