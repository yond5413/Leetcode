class ListNode:
    def __init__(self,val = 0,prev = None,next = None):
        self.value = val
        self.prev = prev
        self.next = next
class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.size = 0
        self.head,self.tail = ListNode(),ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    ###########################
    def insert(self,node):
        prev,next = self.tail.prev,self.tail
        node.next = next
        node.prev = prev
        prev.next = node
        next.prev = node
    def remove(self,node):
        prev,next = node.prev,node.next
        prev.next = next
        next.prev = prev
    ###########################

    def enQueue(self, value: int) -> bool:
        if self.cap >self.size:
            newNode = ListNode(val = value)
            self.size +=1
            self.insert(newNode)
            return True
        return False

    def deQueue(self) -> bool:
        if self.size>0:
            evict = self.head.next
            self.size -=1
            self.remove(evict)
            return True
        return False


    def Front(self) -> int:
        return self.head.next.value if self.size else -1

    def Rear(self) -> int:
        return self.tail.prev.value if self.size else -1

    def isEmpty(self) -> bool:
        return 0 == self.size 

    def isFull(self) -> bool:
         return self.cap == self.size 


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()