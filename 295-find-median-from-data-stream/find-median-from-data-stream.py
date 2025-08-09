import heapq
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left,num*-1)
        if self.left and self.right and (self.left[0]*-1>self.right[0]):
            val = heapq.heappop(self.left)
            heapq.heappush(self.right,val*-1)
        #########################################
        if len(self.left)+1 < len(self.right):
            val = heapq.heappop(self.right)
            heapq.heappush(self.left,val*-1)
        if len(self.left) > len(self.right)+1:
            val = heapq.heappop(self.left)
            heapq.heappush(self.right,val*-1)
    def findMedian(self) -> float:
        if len(self.left)>len(self.right):
            return self.left[0]*(-1)
        if len(self.left)<len(self.right):
            return self.right[0]
        return (self.left[0]*(-1)+self.right[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()