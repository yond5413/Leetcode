from typing import Optional
'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''
'''
### Solution  notes
Easy problem intuition kind of carries us through it 
- Essentially just check if list1 and list2 current node is not none and compare 
then just set curr.next to the smaller of the two to have the head of the returned list mode have the values in ascending order
- then once one of the nodes is none we can just set curr.next to the other listnode that is not none
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        while(list1!= None and list2 != None):
            print(f"list1: {list1.val}, list2: {list2.val}, list1.next: {list1.next}, list2.next: {list2.next} \n")
            if list1.val >= list2.val:
                print("comparison 1 of while")
                curr.next = list2
                list2 = list2.next
            elif list1.val <= list2.val:
                print("comparison 2 of while")
                curr.next = list1
                list1 = list1.next
            curr = curr.next
        
        print(f"before other conditionals: {head}")
        if list1 != None:
            print(head)
            print("list1 is not none lol")
            curr.next = list1
        if list2 != None:
            curr.next = list2
            print(head)
            print("list2 is not none lol")
        
        return head.next 