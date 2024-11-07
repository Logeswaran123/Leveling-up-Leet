/*

---
MEDIUM
143. Reorder List
---

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000

*/

// Solution 1
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
    void reorderList(ListNode* head) {
        if (!head || !head->next) return;

        // Step 1: Find the middle of linked list using slow and fast pointer technique
        ListNode* slow = head;
        ListNode* fast = head->next;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // Step 2: Split the list into two halves
        ListNode* second_half = slow->next;
        slow->next = nullptr;  // End the first half of the list

        // Step 3: Reverse second half of the list
        ListNode* prev = nullptr;
        ListNode* current = second_half;
        while (current) {
            ListNode* tmp = current->next;
            current->next = prev;
            prev = current;
            current = tmp;
        }

        // Step 4: Merge the two halves
        ListNode* first_half = head;
        second_half = prev; // The reversed second half
        while (second_half) {
            ListNode* tmp1 = first_half->next;
            ListNode* tmp2 = second_half->next;
            first_half->next = second_half;
            second_half->next = tmp1;
            first_half = tmp1;
            second_half = tmp2;
        }
    }
};