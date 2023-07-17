'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]
 
Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''
from typing import Optional
#-> some hidden import leetcode uses
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
###########################
# Solution Summary
'''
Given cases like with linked list l1 having values of 1234 and l2 having 567 the lengths of each are potentially equal
Therefore to account for this I had to iterate through each linked list then sum the total then create a new linked list for the result
O(m+n) time complexity
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_value = self.ValToInt(l1)
        l2_value = self.ValToInt(l2)
        res = str(l1_value+l2_value)
        ret = ListNode(int(res[0]),None)
        holder = ret
        for i in range(1,len(res)):
            holder.next = ListNode(int(res[i]),None)
            holder = holder.next
        return ret
    ####Helper functions######
    def ValToInt(self, l1: Optional[ListNode]):
        ret = 0
        while(l1 !=None):
            ret*=10
            ret+=l1.val
            l1 = l1.next
        return ret
    ##########################