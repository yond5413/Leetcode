
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
# completion info
#Time Submitted  |  Status   |  Runtime | Memory | Language
#10/04/2022 18:33	Accepted	63 ms	 13.5 MB	python

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0,None)
        temp = ret
        sum = 0
        remainder = 0 
        while(l1 != None or l2 != None):
            a = 0
            b = 0 
            if(l1 != None):
                a =  l1.val
                l1 = l1.next
            if(l2 != None):
                b = l2.val
                l2 = l2.next
            sum = a + b + remainder
            if sum >= 10:
                remainder = 1
                sum = sum-10
            else:
                remainder = 0
            temp.val = sum
            if (l1 != None or l2 != None):
                temp.next = ListNode(0,None)
                temp = temp.next
        if (remainder == 1):
            temp.next = ListNode(1,None)
        return ret