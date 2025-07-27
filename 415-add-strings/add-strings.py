class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ret = ""
        i,j = len(num1)-1,len(num2)-1
        carry = 0
        while (i>=0 and j>=0):
            a,b = int(num1[i]),int(num2[j])
            res = a+b + carry
            carry = res//10
            val = res%10
            ret +=  str(val)
            i-=1
            j-=1
        ##########################
        while i>=0:
            val = int(num1[i]) + carry
            rem = val %10
            carry = val//10
            ret+= str(rem)
            i-=1
        while j>=0:
            val = int(num2[j]) + carry
            rem = val %10
            carry = val//10
            ret+= str(rem)
            j-=1
        if carry:
            ret +=str(carry)
        return ret[::-1]