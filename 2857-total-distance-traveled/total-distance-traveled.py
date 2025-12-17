class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ret = 0
        i = 0
        while mainTank>0:
            ret+= 10
            i+=1
            mainTank-=1
            if i == 5 and additionalTank>0:
                i=0
                additionalTank-=1
                mainTank+=1
        return ret