class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        i = 0
        ret = 0
        while mainTank >0:
            mainTank-=1
            ret+=10
            i+=1
            if i==5 and additionalTank>0:
                additionalTank-=1
                mainTank+=1
                i =0
        return ret