class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        ret = r
        while(l<=r):
            mid = (r+l)//2
            k = 0
            for p in piles:
                k += math.ceil(p/mid)
            if k <=h:
                ret = mid
                r =mid-1
            else:
                l = mid+1
        return ret
