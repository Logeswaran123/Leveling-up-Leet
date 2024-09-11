/*

---
EASY
110. Balanced Binary Tree
---

Given a binary tree, determine if it is 
height-balanced
.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104


*/

// Solution 1
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
    pair<bool, int> dfs(TreeNode* root) {
        if (!root) return {true, 0};

        auto left = dfs(root->left);
        auto right = dfs(root->right);

        bool balanced = left.first && right.first && abs(left.second - right.second) <= 1;
        int height = max(left.second, right.second) + 1;

        return {balanced, height};
    }

    bool isBalanced(TreeNode* root) {
        return dfs(root).first; // height-balanced binary tree
    }
};