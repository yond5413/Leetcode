/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        if (head == nullptr || head->next == nullptr){
            return nullptr;
        }
        ListNode dummy = ListNode();
        dummy.next = head;
        ListNode* slow = &dummy;//head;
        ListNode* fast = &dummy;//head;
        while(fast->next != nullptr && fast->next->next != nullptr){
            slow = slow->next;
            fast = fast->next->next;
            // could have just counted number of jumps ig
        }
        slow->next = slow->next->next;
        slow = slow->next;
        return dummy.next;

    }
};