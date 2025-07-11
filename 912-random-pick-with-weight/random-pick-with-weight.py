import random 
class Solution:

    def __init__(self, w: List[int]):
        self.cum_sum = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.cum_sum.append(prefix_sum)
        self.total = prefix_sum

    def pickIndex(self) -> int:
        choice = random.randint(1,self.total)
        def bin_search(target):
            l,r = 0,len(self.cum_sum)
            while(l<r):
                mid = (l+r)//2
                
                if self.cum_sum[mid] <target:
                    l = mid+1
                else:
                    r = mid
            return l
        ret = bin_search(choice)
        return ret

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()