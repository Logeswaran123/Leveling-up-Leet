/*

---
EASY
572. Subtree of Another Tree
---

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104

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
    bool sameTree(TreeNode* root, TreeNode* subRoot) {
        if (!root && !subRoot) return true;     // end of the trees

        // if current node of both trees are equal, check their left and right subtrees
        if (root && subRoot && root->val == subRoot->val) {
            return sameTree(root->left, subRoot->left) && sameTree(root->right, subRoot->right);
        }

        return false;
    }

    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (!subRoot) return true;  // if subRoot tree is empty

        if (!root) return false;    // if root tree is empty

        if (sameTree(root, subRoot)) return true;   // if root tree and subRoot tree are same

        // Check if left or right subtree of root tree is same as subRoot tree
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }
};