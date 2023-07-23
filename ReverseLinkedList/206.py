from typing import Optional
'''

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode()
        storage = []
        if head == None:
            return head
        while(head != None):
            storage.append(head.val)
            head = head.next
        curr = ret
        for i in range(1,len(storage)+1):
            curr.val = storage[-i]
            if i != len(storage):
                curr.next = ListNode()
                curr = curr.next
        return ret