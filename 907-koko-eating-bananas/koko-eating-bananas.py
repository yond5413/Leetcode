class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        ret = r
        while (l<=r):
            k = (r+l)//2
            tot = 0
            for p in piles:
                tot+= math.ceil(p/k)
            if tot >h:
                l = k+1
            else:
                ret = k
                r = k-1
        return ret