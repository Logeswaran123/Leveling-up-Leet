"""

---
MEDIUM
98. Validate Binary Search Tree
---

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1

"""

## Solution 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def valid(self, node, minimum, maximum):
        if not node:
            return True

        if not (minimum < node.val < maximum):
            return False

        return self.valid(node.left, minimum, node.val) and self.valid(node.right, node.val, maximum)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, float('-inf'), float('inf'))

## Solution 2
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

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        nodes = []
        # Get the in-order traversal of the tree
        self.inorder(root, nodes)

        # Check if there are duplicates
        if len(nodes) != len(set(nodes)):
            return False

        # Check if the list is sorted in ascending order
        for i in range(len(nodes) - 1):
            if nodes[i] >= nodes[i + 1]:
                return False

        return True
