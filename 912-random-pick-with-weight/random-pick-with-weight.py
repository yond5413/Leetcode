import random
class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for wi in w:
            total+=wi
            self.prefix.append(total)
        self.total = total

    def pickIndex(self) -> int:
        targ = random.randint(1,self.total)
        l,r = 0,len(self.prefix)
        while(l<r):
            mid = (l+r)//2
            if self.prefix[mid] < targ:
                l = mid+1
            else:
                r = mid
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()