class MovingAverage:

    def __init__(self, size: int):
        self.cap = size
        self.window = []
        self.sum = 0
    def next(self, val: int) -> float:
        
        self.window.append(val)
        self.sum +=val
        if len(self.window) >self.cap: 
            rem = self.window.pop(0)
            self.sum-=rem
        ret = self.sum/len(self.window)
        return ret


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)