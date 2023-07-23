from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
##### Solution notes#####
essentially instead of using the list like I did previously I used some place holder variables 
- temp stores next listnode
- curr.next replaced with prev (initially set to none)
- prev is set to curr 
- and curr is set to temp which stores the inital curr.next, curr = temp = old (curr.next)
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr = None, head
        while(curr != None):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            #print(f"temp: {temp}, curr: {curr}, curr.next: {curr.next}, prev: {prev}/n")   
        return prev