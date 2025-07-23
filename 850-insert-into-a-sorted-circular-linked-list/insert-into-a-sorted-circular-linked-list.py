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
        def helper(curr,next,new):
            curr.next = new
            new.next = next

        curr = head
        while curr.next != head:

            if curr.val <= insertVal and insertVal<= curr.next.val:
                helper(curr,curr.next,new_node)
                return head
            elif curr.val >curr.next.val:
                print(f"curr:{curr.val},insert:{insertVal},next:{curr.next.val}")
                if curr.next.val>=insertVal or insertVal >=curr.val:
                    print('tears')
                    helper(curr,curr.next,new_node)
                    return head
            curr = curr.next
        print(f"curr:{curr.val},next:{curr.next.val}")
        helper(curr,curr.next,new_node)
        return head