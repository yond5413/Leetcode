class ListNode:
    def __init__(self,value = 0,prev = None,next = None):
        self.value = value
        self.prev = prev
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.size = 0
        self.head,self.tail = ListNode(),ListNode()
        self.head.next,self.tail.prev, = self.tail,self.head
    ####################################
    def insert(self,node):
        prev,next = self.tail.prev,self.tail
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next
    def remove(self,node):
        prev,next = node.prev,node.next
        prev.next = next
        next.prev = prev
    ####################################
    def enQueue(self, value: int) -> bool:
        if self.cap>self.size:
            newNode = ListNode(value = value)
            self.size +=1
            self.insert(newNode)
            return True
        return False

    def deQueue(self) -> bool:
        if self.size>0:
            evict = self.head.next
            self.remove(evict)
            self.size -=1
            return True
        return False

    def Front(self) -> int:
        return self.head.next.value if self.size else -1 

    def Rear(self) -> int:
        return self.tail.prev.value if self.size else -1 

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()