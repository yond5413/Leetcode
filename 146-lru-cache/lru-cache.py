class ListNode:
    def __init__(self,key=0,val=0,prev=None,next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.lookup = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity
    ##########################################
    # LinkedList helpers
    def insert(self,node):
        prev,next = self.tail.prev,self.tail
        prev.next = node
        next.prev = node
        node.next,node.prev = next,prev
    def remove(self,node):
        prev,next = node.prev,node.next
        prev.next = next
        next.prev = prev
    ##########################################
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
        new_node = ListNode(key,value)
        self.lookup[key] = new_node
        self.insert(new_node)
        if len(self.lookup) > self.cap:
            evict = self.head.next
            self.remove(evict)
            self.lookup.pop(evict.key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)