class Node:
    def __init__(self,key=0,val=0,prev=None,next=None):
        self.key = key 
        self.val = val
        self.prev = prev
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.head,self.tail = Node(),Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.lookup = {}
    #########################
    def insert(self,curr):
        prev,next = self.head,self.head.next
        prev.next = curr
        next.prev = curr
        curr.next = next
        curr.prev = prev
    def remove(self,curr):
        prev,next = curr.prev,curr.next
        prev.next = next
        next.prev = prev
    #########################
    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        ret = self.lookup[key]
        self.remove(ret)
        self.insert(ret)
        return ret.val

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.remove(self.lookup[key])
        newNode = Node(key,value)
        self.insert(newNode)
        self.lookup[key] = newNode
        if self.cap < len(self.lookup):
            lru = self.tail.prev
            self.lookup.pop(lru.key)
            self.remove(lru)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)