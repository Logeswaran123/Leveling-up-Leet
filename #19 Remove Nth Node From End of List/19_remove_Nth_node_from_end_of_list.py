"""

---
MEDUM
19. Remove Nth Node From End of List
---

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

"""

## Solution 1
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        vals = []
        curr = head
        while curr.next != None:
            vals.append(curr.val)
            curr = curr.next
        vals.append(curr.val)
        del vals[-n]

        if len(vals) == 0:
            return head.next

        new_head = ListNode(val=vals[0])
        curr = new_head
        for num in vals[1:]:
            new_node = ListNode(val=num)
            curr.next = new_node
            curr = curr.next
        return new_head