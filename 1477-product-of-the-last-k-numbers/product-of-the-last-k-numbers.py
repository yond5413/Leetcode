class ProductOfNumbers:

    def __init__(self):
        self.stream = []
    def add(self, num: int) -> None:
        self.stream.append(num)
        if num == 1:
            return
        if num ==0:
            self.stream = [0]*(len(self.stream))
            return
        for i in range(len(self.stream)-1):
            self.stream[i]*=num    

    def getProduct(self, k: int) -> int:
        '''if len(self.stream) <k:
            return -1'''
        return self.stream[len(self.stream)-k]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)