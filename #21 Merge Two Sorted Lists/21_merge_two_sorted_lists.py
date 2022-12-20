"""

---
EASY
21. Merge Two Sorted Lists
---

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

"""

## Solution 1
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None and list2 == None:
            return list1
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        merged_list = ListNode()
        head = merged_list

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                node = ListNode(val=list1.val)
                head.next = node
                head = head.next
                list1 = list1.next
            elif list1.val > list2.val:
                node = ListNode(val=list2.val)
                head.next = node
                head = head.next
                list2 = list2.next
            else: # list1.val == list2.val
                node = ListNode(val=list1.val)
                head.next = node
                head = head.next
                list1 = list1.next
                node = ListNode(val=list2.val)
                head.next = node
                head = head.next
                list2 = list2.next

        while list1 != None:
            node = ListNode(val=list1.val)
            head.next = node
            head = head.next
            list1 = list1.next

        while list2 != None:
            node = ListNode(val=list2.val)
            head.next = node
            head = head.next
            list2 = list2.next

        return merged_list.next


## Solution 2
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 and list2:
            if list1.val > list2.val:
                list1, list2 = list2, list1
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1 or list2


## Solution 3
