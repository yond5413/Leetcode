class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        new_range = [-3000,0]
        if self.queue:
            new_range[0] = new_range[0]+t
            new_range[1] = t
            while self.queue and self.queue[0]<new_range[0]:
                self.queue.pop(0)
        self.queue.append(t)
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)