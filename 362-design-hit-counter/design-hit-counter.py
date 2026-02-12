class HitCounter:

    def __init__(self):
        self.queue = []

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # return timesamp-300 
        if timestamp-300<=0:
            return len(self.queue)
        while(self.queue):
            if self.queue[0] <=timestamp-300:
                self.queue.pop(0)
            else: 
                break
        return len(self.queue)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)