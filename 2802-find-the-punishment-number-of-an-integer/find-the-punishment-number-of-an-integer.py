class Solution:
    def punishmentNumber(self, n: int) -> int:
        ret = 0
        def helper(idx: int,curr: int,targ: int,s: str):
            if idx == len(s) and targ == curr:
                return True
            for i in range(idx,len(s)):
                if helper(i+1,curr+int(s[idx:i+1]),targ,s):
                    return True
            return False
            
        for i in range(1,n+1):
            if helper(0,0,i,str(i**2)):
                ret+= i**2
        return ret