/*

---
HARD
124. Binary Tree Maximum Path Sum
---

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000

*/

// Solution 1
//   Important Problem: Best to understand the logic
//
// Example Tree:
//       -10
//       /  \
//      9    20
//          /  \
//         15   7
//
// Step 1: Initialize max_sum to root.
// We start our traversal from the root (-10).
// Step 2: Explore the left subtree of the root (-10):
// - The left child is 9:
//   - 9 has no children, so both left and right gains are 0.
//   - Calculate current_path_sum for 9: 9 + 0 + 0 = 9.
//   - Update max_sum to 9 (since 9 > -10).
//   - Return the value of 9 to its parent (-10).
// Step 3: Explore the right subtree of the root (-10):
// - The right child is 20:
//   - Explore the left child of 20 (which is 15):
//     - 15 has no children, so both left and right gains are 0.
//     - Calculate current_path_sum for 15: 15 + 0 + 0 = 15.
//     - Update max_sum to 15 (since 15 > 9).
//     - Return the value of 15 to its parent (20).
//   - Explore the right child of 20 (which is 7):
//     - 7 has no children, so both left and right gains are 0.
//     - Calculate current_path_sum for 7: 7 + 0 + 0 = 7.
//     - max_sum remains 15 (since 7 < 15).
//     - Return the value of 7 to its parent (20).
//   - Now back to node 20:
//     - Left gain = 15 (returned from 15), Right gain = 7 (returned from 7).
//     - Calculate current_path_sum for 20: 20 + 15 + 7 = 42.
//     - Update max_sum to 42 (since 42 > 15).
//     - Return the value of 20 + max(15, 7) = 20 + 15 = 35 to its parent (-10).
// Step 4: Now back to the root (-10):
// - Left gain = 9 (returned from 9), Right gain = 35 (returned from 20).
// - Calculate current_path_sum for -10: -10 + 9 + 35 = 34.
// - max_sum remains 42 (since 34 < 42).
// - Return the value of -10 + max(9, 35) = -10 + 35 = 25, but this return value is not used further since the traversal is complete.
// Step 5: The traversal is now complete, and the maximum path sum found is stored in max_sum, which is 42.
//
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
    // Return max path without split
    int dfs(TreeNode* node, int& max_sum) {
        if (!node) return 0;

        // Recursively compute maximum path of left and right subtrees
        int left_max = max(dfs(node->left, max_sum), 0);
        int right_max = max(dfs(node->right, max_sum), 0);

        // Get max path with split / compare without split to get global maximum path
        max_sum = max(max_sum, node->val + left_max + right_max);

        return node->val + max(left_max, right_max);
    }

    int maxPathSum(TreeNode* root) {
        int max_sum = root->val;
        dfs(root, max_sum);
        return max_sum;
    }
};