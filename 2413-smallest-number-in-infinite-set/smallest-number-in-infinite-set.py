import heapq as hq
class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.lookup = set()
        self.curr = 1
    def popSmallest(self) -> int:
        if self.heap:
            ret = hq.heappop(self.heap)
            self.lookup.remove(ret)
        else:
            ret = self.curr
            self.curr+=1
        return ret

    def addBack(self, num: int) -> None:
        if self.curr > num and num not in self.lookup:
            self.lookup.add(num)
            hq.heappush(self.heap,num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)