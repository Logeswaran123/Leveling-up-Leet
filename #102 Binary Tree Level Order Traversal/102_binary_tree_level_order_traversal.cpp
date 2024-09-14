/*

---
MEDIUM
102. Binary Tree Level Order Traversal
---

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        deque<TreeNode*> q;

        if (root) q.push_back(root);

        while (!q.empty()) {
            vector<int> sublist;

            for (int i = 0, len = q.size(); i < len; i++) { // Important: Note the Loop statement
                TreeNode* node = q.front();
                q.pop_front();
                sublist.push_back(node->val);

                if (node->left) q.push_back(node->left);
                if (node->right) q.push_back(node->right);
            }

            res.push_back(sublist);
        }

        return res;
    }
};

// Solution 2
// Little mode readable and optimized
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (!root) return {};

        vector<vector<int>> res;
        deque<TreeNode*> q = {root};

        while (!q.empty()) {
            vector<int> sublist;
            int level_length = q.size();  // Get current level size

            for (int i = 0; i < level_length; ++i) {
                TreeNode* node = q.front();
                q.pop_front();
                sublist.push_back(node->val);

                // Push left and right children if they exist
                if (node->left) q.push_back(node->left);
                if (node->right) q.push_back(node->right);
            }

            res.push_back(sublist);
        }

        return res;
    }
};