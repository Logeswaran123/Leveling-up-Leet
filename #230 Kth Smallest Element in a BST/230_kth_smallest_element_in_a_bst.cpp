/*

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

*/

// Solution 1
/*
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
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> stack;
        TreeNode* curr = root;

        while (!stack.empty() || curr != nullptr) {
            // Traverse to the leftmost node
            while (curr != nullptr) {
                stack.push(curr);
                curr = curr->left;
            }

            // Process the node
            curr = stack.top();
            stack.pop();
            k--;

            // If k reaches 0, we found the k-th smallest element
            if (k == 0) {
                return curr->val;
            }

            // Move to the right subtree
            curr = curr->right;
        }

        return -1; // Return -1 if k is invalid
    }
};