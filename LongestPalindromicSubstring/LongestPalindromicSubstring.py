'''
Given a string s, return the longest 
palindromic
 
substring
 in s.

 
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = ""
        if (len(s) < 2):
            return s
        ####################
        ## actual logic
        inner = 0 
        outter = 0
        palindromeSize = 0
        for i in range(0,len(s)):
            if len(s[i:]) > palindromeSize:
                for k in range(len(s)+1,i,-1):
                    flag = checkPalindrome(s,i,k)
                    if flag == True:
                            if len(s[i:k]) >palindromeSize: 
                                inner = i
                                outter = k
                                palindromeSize = len(s[i:k])
            else:
                break
        ret = s[inner:outter]
        if len(ret) == 0:
            ret = s[0]  
        return ret
##########################################        
def checkPalindrome(s,i,j) -> bool:
    ################################
    ## s = string 
    ## i = int (inner bound of array)
    ## j = int (outer bound of array)
    ## ASSUMING i>=0 and j<len(s) UNLESS SPECIFIED OTHERWISE
        ''' sub1 = ""
        sub2 = ""
        for x in range(i,j):
            sub1 = sub1 + s[x]
        for x in range(j,i):
            sub2 = sub2+s[x]'''
        sub1 = s[i:j]#"" #regular
        #newstr = s[::-1] #flips string lol just learned this today 
        #sub2 = newstr[i:j]#"" # opposite
        sub2 = sub1[::-1]
        if sub1 == sub2: 
            return True
        else:
            return False 
    ################################