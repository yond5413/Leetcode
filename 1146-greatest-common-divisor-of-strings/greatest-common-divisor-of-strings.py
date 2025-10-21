class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m,n = len(str1),len(str2)
        min_r = min(m,n)
        for r in range(min_r,0,-1):
            if m%r ==0 and n%r ==0:
                curr = str1[:r]
                if curr*(m//r) ==str1 and curr*(n//r) ==str2:
                    return curr
        return ""