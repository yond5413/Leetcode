# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #########################
        prev,curr = None,slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        ###########################
        ret = 0
        first = head
        second = prev
        while second:
            curr = first.val+second.val
            ret = max(ret,curr)
            first = first.next
            second = second.next
        return ret