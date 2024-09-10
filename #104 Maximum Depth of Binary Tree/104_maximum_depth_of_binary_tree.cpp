/*

---
EASY
104. Maximum Depth of Binary Tree
---

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100


*/

// Solution 1
// DFS with Recursion
/**
 * Let's consider this simple binary tree:
 *
 *      1
 *     / \
 *    2   3
 *
 * The goal is to find the maximum depth (height) of this tree. 
 * The maximum depth is the longest path from the root node (1) 
 * down to the farthest leaf node (either 2 or 3 in this case).
 *
 * How the recursion works for our example tree:
 * 
 * 1. We start at the root node (1).
 *    - We need to find the depth of both the left (2) and right (3) subtrees.
 * 
 * 2. For the left subtree (node 2):
 *    - Both left and right children of node 2 are null, so the function returns 0 for both.
 *    - The depth for node 2 is max(0, 0) + 1 = 1.
 * 
 * 3. For the right subtree (node 3):
 *    - Similarly, both left and right children of node 3 are null, so the function returns 0 for both.
 *    - The depth for node 3 is max(0, 0) + 1 = 1.
 * 
 * 4. Back at the root node (1):
 *    - The depth of the left subtree is 1 (from node 2).
 *    - The depth of the right subtree is 1 (from node 3).
 *    - The maximum depth of the tree is max(1, 1) + 1 = 2.
 * 
 * So, the maximum depth of this binary tree is 2.
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
    int maxDepth(TreeNode* root) {
        if (!root) return 0; // Reached the leaf node or root is nullptr
        return max(maxDepth(root->left), maxDepth(root->right)) + 1;
    }
};

// Solution 2
// BFS
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
    int maxDepth(TreeNode* root) {
        if (!root) return 0;

        std::queue<TreeNode*> q;
        q.push(root);
        int level = 0;

        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; ++i) {
                TreeNode* node = q.front();
                q.pop();
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            ++level;
        }

        return level;
    }
};

// Solution 3
// Iterative DFS
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
    int maxDepth(TreeNode* root) {
        if (!root) return 0;

        std::stack<std::pair<TreeNode*, int>> stack;
        stack.push({root, 1});
        int res = 0;

        while (!stack.empty()) {
            auto [node, depth] = stack.top();
            stack.pop();

            if (node) {
                res = std::max(res, depth);
                stack.push({node->left, depth + 1});
                stack.push({node->right, depth + 1});
            }
        }

        return res;
    }
};