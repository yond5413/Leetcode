class Node: 
    def __init__(self,key = 0,val=0,next=None,prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.lookup = {} 
        self.head,self.tail = Node(),Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    ##########################
    def insert(self,curr):
        prev,next = self.head,self.head.next
        curr.prev,curr.next = prev,next
        prev.next = curr
        next.prev = curr
    def remove(self,curr):
        prev,next = curr.prev,curr.next
        prev.next = next
        next.prev = prev
    ##########################
    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        curr = self.lookup[key]
        self.remove(curr)
        self.insert(curr)
        return curr.val
    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.remove(self.lookup[key])
        newNode = Node(key,value)
        self.lookup[key] = newNode
        self.insert(newNode)
        if self.cap <len(self.lookup):
            lru = self.tail.prev
            self.lookup.pop(lru.key)
            self.remove(lru)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)