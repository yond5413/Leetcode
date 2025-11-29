/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function deleteMiddle(head: ListNode | null): ListNode | null {
    if (head ===null){
        return null;
    }
    let dummy = new ListNode(0,head);
    let slow = dummy
    let fast = dummy
    while (fast.next && fast.next.next){
        slow = slow.next
        fast = fast.next.next
    }
    slow.next = slow.next.next
    return dummy.next
};