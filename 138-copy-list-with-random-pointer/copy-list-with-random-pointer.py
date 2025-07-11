"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        lookup = {}
        curr = head
        while curr:
            lookup[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                lookup[curr].next = lookup[curr.next]
            if curr.random:
                lookup[curr].random = lookup[curr.random]
            curr = curr.next
        return lookup[head]