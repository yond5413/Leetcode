import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.lookup = set()
        self.heap = []
        for i in range(1,1001):
            self.lookup.add(i)
            self.heap.append(i)

    def popSmallest(self) -> int:
        #print(f"heap:{self.heap}, set:{self.lookup}")
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.lookup.remove(smallest)
            return smallest
        return -1

    def addBack(self, num: int) -> None:
        #print(f"heap:{self.heap}, set:{self.lookup}")
        if num not in self.lookup:
            heapq.heappush(self.heap,num)
            self.lookup.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)