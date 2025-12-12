class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ret = 0
        used =0
        while(mainTank>0):
            used+=1
            ret+=10
            mainTank-=1
            if used == 5 and additionalTank>0:
                used = 0
                mainTank+=1
                additionalTank-=1
        return ret