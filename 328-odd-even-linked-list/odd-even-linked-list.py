# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        ##################3
        odd = head
        even_head = even=head.next
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            # take every other one for even/odd
            even = even.next
            odd = odd.next
        odd.next = even_head
        return head
