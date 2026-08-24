# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ret = 0
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        ###################
        curr,prev = slow,None
        while curr:
            temp = curr.next
            curr.next = prev
            prev =curr
            curr = temp
        ###################
        l,r = head,prev
        while r:
            val = l.val+r.val
            ret = max(ret,val)
            l = l.next
            r = r.next
        return ret