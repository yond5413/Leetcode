from typing import Optional
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode()
        l1_sum = (self.ValToInt(l1))
        l2_sum = (self.ValToInt(l2))
        res = str(l1_sum + l2_sum)
        ### use -i to access str backwards
        holder = ret
        for i in range(1, len(res)+1):
            holder.val = int(res[-i])
            if i == len(res):
                holder.next = None
                break
            holder.next = ListNode()
            holder = holder.next
        return ret
    ####Helper functions######
    def ValToInt(self, l1: Optional[ListNode]):
        ret = 0
        if l1!= None:
            ret = l1.val
        count = 1
        while(l1.next !=None):
            ret+=(l1.next.val)*(10**count)
            count+=1
            l1 = l1.next
        return ret
    ##########################