/*

---
MEDIUM
1448. Count Good Nodes in Binary Tree
---

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

 

Example 1:



Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:



Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
 

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].

*/

// Solution 1
// Logic:
// Total good nodes = 1 (root) + good nodes in left subtree + good nodes in right subtree
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
    int dfs(TreeNode* node, int max_val) {
        if (!node) return 0;     // breaking condition: node is null

        // Check if the current node is a "good" node
        int good = (node->val >= max_val) ? 1 : 0;   // 1 If node value is greater than maximum of its parent nodes, else 0

        max_val = max(max_val, node->val);
        good += dfs(node->left, max_val);   // left subtree
        good += dfs(node->right, max_val);  // right subtree
        return good;
    }

    int goodNodes(TreeNode* root) {
        if (!root) return 0;
        return dfs(root, root->val);    // Start from the first node
    }
};