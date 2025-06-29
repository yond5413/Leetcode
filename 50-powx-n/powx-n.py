class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        elif n<0:
            return 1/self.myPow(x,-n)
        ret = 1
        while(n>0):
            if n%2==0:
                x*=x
                n=n//2
            else:
                ret*=x
                n-=1
        return ret