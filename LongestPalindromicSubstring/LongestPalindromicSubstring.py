class Solution:
    def checkPalindrome(self,s,i,j): -> bool
    ################################
    ## s = string 
    ## i = int (inner bound of array)
    ## j = int (outer bound of array)
    ## ASSUMING i>=0 and j<len(s) UNLESS SPECIFIED OTHERWISE
    sub1 = s[i:j]#"" #regular
    newstr = s[::-1] #flips string lol just learned this today 
    sub2 = newstr[i:j]#"" # opposite
    '''for x in range(i,j):
        sub1 = sub1 + 
    for x in range(j,i):
        sub2 = sub2+s[x]'''
    if sub1 == sub2 
        return True
    else:
        return False 
    ################################
    def longestPalindrome(self, s: str) -> str:
        ret = ""
        if (len(a) < 2):
            return s
        ####################
        ## actual logic
        for i in range 
        return ret 