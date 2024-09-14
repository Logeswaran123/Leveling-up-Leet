"""

---
MEDIUM
230. Kth Smallest Element in a BST
---

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

"""

## Solution 1
"""
Iterative Solution:

Step-by-Step Example

Consider the following BST:
        5
       / \
      3   6
     / \
    2   4
   /
  1

If k = 4, we want to find the 4th smallest element.

1. **Initialization**:
   - Create an empty stack: stack = []
   - Set curr to the root of the tree (5).

2. **First While Loop** (Traversing to the leftmost node):
   - Push 5 to the stack: stack = [5], move curr to 3.
   - Push 3 to the stack: stack = [5, 3], move curr to 2.
   - Push 2 to the stack: stack = [5, 3, 2], move curr to 1.
   - Push 1 to the stack: stack = [5, 3, 2, 1], move curr to None (since 1 has no left child).

3. **Processing Nodes** (Second While Loop - Stack Popping):
   - First pop: Pop 1 from the stack: stack = [5, 3, 2], decrement k to 3. Move curr to the right of 1, which is None.
   - Second pop: Pop 2 from the stack: stack = [5, 3], decrement k to 2. Move curr to the right of 2, which is None.
   - Third pop: Pop 3 from the stack: stack = [5], decrement k to 1. Move curr to the right of 3, which is 4.
   - Fourth pop: Push 4 to the stack: stack = [5, 4], move curr to None (since 4 has no left child). Pop 4 from the stack: stack = [5], decrement k to 0.
     Since k is now 0, return the value of the current node, which is 4.

4. **Result**:
   The 4th smallest element in this BST is 4.
"""
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

## Solution 2
## Recursive Solution
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, nodes):
        if not root:
            return

        self.inorder(root.left, nodes)
        nodes.append(root.val)
        self.inorder(root.right, nodes)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return True

        nodes = []
        # Get the in-order traversal of the tree
        self.inorder(root, nodes)

        # Check if there are duplicates
        if len(nodes) != len(set(nodes)):
            return False

        return nodes[k-1]