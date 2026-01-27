class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = [i for i in s if i.isalnum()]
        l,r = 0,len(clean)-1
        while(l<=r):
            if clean[l].lower() != clean[r].lower():
                return False
            l+=1
            r-=1
        return True