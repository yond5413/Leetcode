"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        new_node = Node(insertVal)
        if not head:
            new_node.next = new_node
            return new_node
        def add(curr,nex,new):
            curr.next = new
            new.next = nex
        curr = head
        while curr.next!=head:
            if curr.val<= insertVal and curr.next.val>= insertVal:
                add(curr,curr.next,new_node)
                return head
            elif curr.val>curr.next.val:
                if curr.val<= insertVal or curr.next.val>=insertVal:
                    add(curr,curr.next,new_node)
                    return head
            curr = curr.next
        add(curr,curr.next,new_node)
        return head