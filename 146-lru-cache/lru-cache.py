class ListNode:
    def __init__(self,key=0,val=0,prev=None,next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.head,self.tail = ListNode(),ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    #########################################
    def insert(self,node):
        prev,next = self.head,self.head.next
        node.prev,node.next = prev,next
        prev.next = node
        next.prev = node
    def remove(self,node):
        prev,next = node.prev,node.next
        prev.next = next
        next.prev = prev

    #########################################
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        curr = self.cache[key]
        self.remove(curr)
        self.insert(curr)
        return curr.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = ListNode(key=key,val=value)
        self.cache[key] = node
        self.insert(node)
        if self.cap <len(self.cache):
            evict = self.tail.prev
            self.remove(evict)
            self.cache.pop(evict.key)



        
    

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)