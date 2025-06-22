class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(cur):
            l,r = 0,len(cur)-1
            while(l<r):
                if cur[l]!=cur[r]:
                    return False
                l+=1
                r-=1
            return True
        l,r = 0,len(s)-1
        while(l<r):
            if s[l]!=s[r]:
                return isPalindrome(s[l+1:r+1]) or isPalindrome(s[l:r])    
            l+=1
            r-=1
        return True
        