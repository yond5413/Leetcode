# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return ListNode()
        if not l1 or not l2:
            return l1 if l1 else l2
        curr = ListNode()
        ret = curr
        carry = 0
        while l1 and l2:
            temp = l1.val+l2.val+carry
            val = temp%10
            carry = temp//10
            curr.val = val
            if l1.next or l2.next:
                next = ListNode()
                curr.next = next
                curr = curr.next
            l1,l2 = l1.next,l2.next
        #############################
        while l1:
            temp = l1.val+carry
            val = temp%10
            carry = temp//10
            curr.val = val
            if l1.next :
                next = ListNode()
                curr.next = next
                curr = curr.next
            l1 = l1.next
        while l2:
            temp = l2.val+carry
            val = temp%10
            carry = temp//10
            curr.val = val
            if l2.next:
                next = ListNode()
                curr.next = next
                curr = curr.next
            l2 = l2.next
        if carry:
            curr.next = ListNode(carry)
        return ret