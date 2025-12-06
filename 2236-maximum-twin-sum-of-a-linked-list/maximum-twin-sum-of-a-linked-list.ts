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

function pairSum(head: ListNode | null): number {
    let slow = head
    let fast = head
    while (fast !== null && fast.next !== null){
        slow = slow.next
        fast = fast.next.next
    }
    //////////////////
    let prev:ListNode|null = null
    let curr:ListNode|null = slow
    while (curr){  
        let temp: ListNode|null = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    }
    //////////////////
    let ret:number = 0
    let first:ListNode|null = head
    let second:ListNode|null = prev
    while (second){
        let curr:number  = first.val+second.val
        ret = Math.max(ret,curr)
        first = first.next
        second = second.next
    }
    const foo = () => console.log("hello world")
    foo();
    return ret

};